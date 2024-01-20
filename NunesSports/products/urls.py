from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path('', views.products, name = 'products'),
    path('registred_products/', views.registred_products, name = 'registred_products'),
    path('<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('<int:product_id>/delete/', views.delete_product, name='delete_product'),
]