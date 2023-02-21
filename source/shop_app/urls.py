from django.urls import path
from .views import ProductList, ProductCreate, ProductDelete, ProductUpdate, ProductView, CategoryList, CategoryCreate, CategoryUpdate, CategoryDelete

urlpatterns = [
    path('', ProductList.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductView.as_view(), name='product_detail'),
    path('products/add/', ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/edit', ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDelete.as_view(), name='product_delete'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/add/', CategoryCreate.as_view(), name='category_create'),
    path('categories/<int:pk>/edit', CategoryUpdate.as_view(), name='category_update'),
    path('categories/<int:pk>/delete', CategoryDelete.as_view(), name='category_delete'),
]
