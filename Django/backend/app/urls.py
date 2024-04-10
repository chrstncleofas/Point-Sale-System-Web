from app import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    # Frontend API for Inventory
    url(r'^inventory$',views.inventoryApiRequest),
    url(r'^inventory/([0-9]+)$',views.inventoryApiRequest),
    
    # Frontend API for Transaction
    path('', views.login_page, name='login_page'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
