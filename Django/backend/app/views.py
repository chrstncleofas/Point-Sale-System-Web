from .models import TableStocks, TableTemp, TableTransaction
from django.http import JsonResponse
from app.serializers import InventorySerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

HOME_URL_PATH = 'app/base.html'
DASHBOARDS_URL_PATH = 'app/dashboard.html'

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
        product=TableStocks.objects.get(product_id=product_data['StudentID'])
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
    
def dashboard(request) -> HttpResponse:
    return render(request, DASHBOARDS_URL_PATH)

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
