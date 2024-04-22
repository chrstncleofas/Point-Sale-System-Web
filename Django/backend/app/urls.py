from app import views
from django.conf.urls import url
from django.urls import path
from .views import LoginView, LogoutView

urlpatterns = [
    # Frontend API for Inventory
    path('inventory/', views.inventoryApiRequest),
    path('inventory/<str:product_id>/', views.inventoryApiRequest),
    # Login API
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    # Frontend API for Transaction
    path('', views.login_page, name='login_page'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('getListOfProduct', views.getListOfProduct, name='getListOfProduct'),
    path('<int:id>/view_items/', views.view_items, name='view_items'),
]
