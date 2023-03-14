from django.core.validators import MinValueValidator
from django.db import models
from django.shortcuts import get_object_or_404


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255, default='Description')

    def __str__(self):
        return self.name


class Shop(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    qty = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    description = models.TextField(max_length=1200)
    image_url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return sum(item.subtotal for item in self.cart_items.all())

    def get_cart_items(self):
        return self.cart_items.all()

    def add(self, shop, quantity=1):
        if not self.id:
            self.save()
        cart_item, created = CartItem.objects.get_or_create(cart=self, shop=shop)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

    def remove(self, shop_id):
        cart_item = get_object_or_404(self.cart_items, shop__id=shop_id)
        cart_item.delete()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.shop}'

    @property
    def subtotal(self):
        return self.quantity * self.shop.price


class Checkout(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
