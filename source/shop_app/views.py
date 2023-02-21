from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop, Category
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import ShopForm, CategoryForm


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


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')
    template_name = 'category_confirm_delete.html'
