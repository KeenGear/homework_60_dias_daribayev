from django import forms
from .models import Shop, Category, CartItem, Checkout


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['title', 'price', 'image_url', 'category', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CartItemForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = CartItem
        fields = ('quantity',)


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['name', 'email', 'address', 'city', 'state', 'zip_code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
