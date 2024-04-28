import json
import jwt, datetime
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from app.serializers import InventorySerializer
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import update_session_auth_hash
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate, login, logout
from .models import TableStocks, TableTemp, TableTransaction, CustomUser
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

HOME_URL_PATH = 'app/base.html'
DASHBOARDS_URL_PATH = 'app/dashboard.html'
ADD_PRODUCT_URL = 'app/addingProduct.html'

@csrf_exempt
def inventoryApiRequest(request, product_id=0) -> (JsonResponse | None):
    # Fetch all Data API
    if request.method=='GET':
        products = TableStocks.objects.all()
        product_serializer=InventorySerializer(products, many=True)
        return JsonResponse(product_serializer.data, safe=False)
    # Create or Add API
    elif request.method=='POST':
        product_data=JSONParser().parse(request)
        product_serializer=InventorySerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    # Update API
    elif request.method=='PUT':
        product_data=JSONParser().parse(request)
        product=TableStocks.objects.get(product_id=product_data['ProductID'])
        product_serializer=InventorySerializer(product, data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    # Delete API
    elif request.method=='DELETE':
        product=TableStocks.objects.get(product_id=product_id)
        product.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def saveTransaction():
    pass

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
        response.delete_cookie('jwt')
        response.data = {
            'message' : 'Logout'
        }
        return response
    
def dashboard(request) -> HttpResponse:
    totalProduct = TableStocks.objects.count()
    users = CustomUser.objects.count()
    return render(
        request,
        DASHBOARDS_URL_PATH, 
        {
            'totalProduct': totalProduct,
            'users': users,
        }
    )

def getListOfProduct(request) -> HttpResponse:
    return render(request, 'app/product-page.html', {
        'getListOfProduct' : TableStocks.objects.all(),
    })

def view_items(request, id) -> HttpResponseRedirect:
    if request.method == 'GET':
        TableStocks.objects.get(pk=id)
    return HttpResponseRedirect(reverse(getListOfProduct))

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
