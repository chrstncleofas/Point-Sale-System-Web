import json
import jwt, datetime
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser
from app.serializers import InventorySerializer
from rest_framework.exceptions import ParseError
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate, login, logout
from .models import TableInventory ,TableTransaction, CustomUser
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

HOME_URL_PATH = 'app/base.html'
DASHBOARDS_URL_PATH = 'app/dashboard.html'
ADD_PRODUCT_URL = 'app/addingProduct.html'

@csrf_exempt
def inventoryApiRequest(request, product_id=0):
    # Fetch all Data API
    if request.method == 'GET':
        products = TableInventory.objects.all()
        product_serializer = InventorySerializer(products, many=True)
        return JsonResponse(product_serializer.data, safe=False)
    # POST API Data to Database
    elif request.method == 'POST':
        product_data = request.POST.copy()
        image_data = request.FILES.get('Image')
        product_data['Image'] = image_data      
        product_serializer = InventorySerializer(data=product_data) 
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(product_serializer.errors, status=400)  
    # Update PUT API
    elif request.method == 'PUT':
        try:
            product_data = JSONParser().parse(request)
        except ParseError as e:
            return JsonResponse({'error': str(e)}, status=400)   
        product_id = product_data.get('ProductID')
        product = TableInventory.objects.get(product_id=product_id)
        product_serializer = InventorySerializer(product, data=product_data)    
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse(product_serializer.errors, status=400)
    # Delete API
    elif request.method == 'DELETE':
        product_id = request.POST.get('ProductID')
        try:
            product = TableInventory.objects.get(product_id=product_id)
            product.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except TableInventory.DoesNotExist:
            return JsonResponse({'error': 'Product does not exist'}, status=404)
    
@csrf_exempt
def saveTransaction(request) -> JsonResponse:
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            required_fields = ['TransactionID', 'ProductID', 'ProductName', 'Qty', 'UnitPrice', 'TotalAmount', 'DateTime', 'CashierName']
            for field in required_fields:
                if field not in data or data[field] is None:
                    return JsonResponse({'error': f'Missing or invalid value for field: {field}'}, status=400)

            TableTransaction.objects.create(
                TransactionID=data['TransactionID'],
                ProductID=data['ProductID'],
                ProductName=data['ProductName'],
                Description=data.get('Description', ''),
                Qty=data['Qty'],
                UnitPrice=data['UnitPrice'],
                TotalAmount=data['TotalAmount'],
                DateTime=data['DateTime'],
                CashierName=data['CashierName']
            )
            return JsonResponse({'message': 'Data saved successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise AuthenticationFailed("Account not found")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Wrong Password")
        
        payload = {
            'id' : user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=68),
            'iat': datetime.datetime.utcnow()

        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }  
        return response
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt', path='/')
        response.data = {
            'message' : 'Logout'
        }
        return response
    
def dashboard(request) -> HttpResponse:
    totalProduct = TableInventory.objects.count()
    users = CustomUser.objects.count()
    transactions = TableTransaction.objects.all()
    itemSold = TableTransaction.objects.count()
    total_sales = sum(float(transaction.TotalAmount) for transaction in transactions)
    return render(
        request,
        DASHBOARDS_URL_PATH, 
        {
            'totalProduct': totalProduct,
            'users': users,
            'itemSold' : itemSold,
            'total_sales': total_sales
        }
    )

def getListOfProduct(request) -> HttpResponse:
    return render(request, 'app/product-page.html', {
        'getListOfProduct' : TableInventory.objects.all(),
    })

def search_products(request):
    query = request.GET.get('search')
    if query:
        products = TableInventory.objects.filter(Q(Category__icontains=query) | 
                                          Q(ProductID__icontains=query) | 
                                          Q(ProductName__icontains=query))
    else:
        products = TableInventory.objects.all()
    return render(request, 'app/product-page.html', {'getListOfProduct': products})

def view_items(request, id) -> HttpResponseRedirect:
    if request.method == 'GET':
        TableInventory.objects.get(pk=id)
    return HttpResponseRedirect(reverse(getListOfProduct))

# Code sa logic ng pagawa kung paano mag add ng products
def addProduct(request) -> HttpResponse:
    if request.method == 'POST':
        product_data = request.POST.copy()
        image_data = request.FILES.get('Image')
        product_data['Image'] = image_data
        product_serializer = InventorySerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            messages.success(request, "Product added successfully!")
            return redirect('getListOfProduct')
        else:
            messages.error(request, "Failed to add product. Please check the form.")
    return render(request, 'app/add-product-page.html')

def login_page(request) -> (HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse):
    if request.method == 'POST':
        username = request.POST.get('login-username')
        password = request.POST.get('login-password')

        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect(dashboard)
        else:
            messages.error(
                request,
                "Incorrect username or password, please check your credentials and try again",
                extra_tags='loginError'
            )
            return redirect(login_page)
        
    return render(request, HOME_URL_PATH)

def logout_view(request) -> HttpResponseRedirect:
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect(login_page)
