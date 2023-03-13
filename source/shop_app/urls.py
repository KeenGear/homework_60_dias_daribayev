from django.urls import path
from .views import ProductList, ProductCreate, ProductDelete, ProductUpdate, \
    ProductView, CategoryList, CategoryCreate, CategoryUpdate, \
    CategoryDelete, cart_detail, CartRemoveView, cart_add, cart_update, checkout, checkout_success

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
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/remove/<int:shop_id>/', CartRemoveView.as_view(), name='cart_remove'),
    path('cart/add/<int:shop_id>/', cart_add, name='cart_add'),
    path('cart/update/<int:item_id>/', cart_update, name='cart_update'),
    path('checkout/', checkout, name='checkout'),
    path('checkout_success/', checkout_success, name='checkout_success')
]
