from django.contrib import admin
from .models import Category, Shop, Cart, CartItem

# Register your models here.
admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Cart)
admin.site.register(CartItem)
