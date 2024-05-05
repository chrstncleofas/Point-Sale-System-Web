from app import views
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from .views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
    # Frontend API for Inventory
    url('inventory/',views.inventoryApiRequest),
    url(r'^inventory/([0-9]+)$',views.inventoryApiRequest),
    # Save Transaction
    path('saveTransaction/', views.saveTransaction, name='saveTransaction'),
    # Login API
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    # Frontend API for Transaction
    path('', views.login_page, name='login_page'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    # 
    path('getListOfProduct', views.getListOfProduct, name='getListOfProduct'),
    path('getTransactionsList', views.getTransactionsList, name='getTransactionsList'),
    path('getUserList', views.getUserList, name='getUserList'),
    # 
    path('<int:id>/view_items/', views.view_items, name='view_items'),
    path('<int:id>/viewInfoUsers/', views.viewInfoUsers, name='viewInfoUsers'),
    # 
    path('addProduct/', views.addProduct, name='addProduct'),
    path('delete_list/<int:id>', views.delete_list, name='delete_list'),
    path('editUser/<int:id>', views.editUser, name='editUser'),
    # 
    path('search-products/', views.search_products, name='search_products'),
    path('<int:id>/viewInfoTransaction/', views.viewInfoTransaction, name='viewInfoTransaction'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
