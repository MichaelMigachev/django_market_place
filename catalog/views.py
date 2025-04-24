from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProductForm



class ProductListView(ListView):
    model = Product
#   путь
# app_name/<model_name>_<action>     имя_приложения/<имя_модели>_<действие>
# catalog/product_list.html

class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'




