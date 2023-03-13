from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Shop, Category, Cart, CartItem
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import ShopForm, CategoryForm, CartItemForm, CheckoutForm


class ProductView(DetailView):
    model = Shop
    template_name = 'product_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['fields'] = ['price', 'image_url', 'category', 'description']
        return context


class ProductList(ListView):
    model = Shop
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Product List'
        context['fields'] = ['title', 'price', 'image_url', 'category', 'description']
        return context


class ProductCreate(CreateView):
    model = Shop
    form_class = ShopForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('products_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Task'
        return context


class ProductUpdate(UpdateView):
    model = Shop
    form_class = ShopForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('products_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Task'
        return context


class ProductDelete(DeleteView):
    model = Shop
    success_url = reverse_lazy('products_list')
    template_name = 'product_confirm_delete.html'


class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')
    template_name = 'category_confirm_delete.html'


def cart_detail(request):
    cart = Cart.objects.first()
    checkout_form = CheckoutForm()
    if request.method == 'POST':
        checkout_form = CheckoutForm(request.POST)
        if checkout_form.is_valid():
            checkout_form.save()

    context = {
        'cart': cart,
        'checkout_form': checkout_form,
    }
    return render(request, 'cart_detail.html', context)


def cart_add(request, shop_id):
    cart = Cart.objects.first()
    if not cart:
        cart = Cart.objects.create()
    shop = get_object_or_404(Shop, id=shop_id)
    cart.add(shop)
    return redirect('cart_detail')


class CartRemoveView(View):
    def get(self, request, shop_id):
        cart = Cart.objects.first()
        cart.remove(shop_id)
        return redirect('cart_detail')

    def post(self, request, shop_id):
        cart = Cart.objects.first()
        cart.remove(shop_id)
        return redirect('cart_detail')


def cart_update(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        form = CartItemForm(request.POST, instance=cart_item)
        if form.is_valid():
            form.save()
            return redirect('cart_detail')
    else:
        form = CartItemForm(instance=cart_item)

    context = {
        'form': form,
        'cart_item': cart_item,
    }
    return render(request, 'cart_update.html', context)


def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            checkout = form.save()
            return redirect('checkout_success')
    else:
        form = CheckoutForm()
    context = {'form': form}
    return render(request, 'checkout.html', context)


def checkout_success(request):
    return render(request, 'checkout_success.html')
