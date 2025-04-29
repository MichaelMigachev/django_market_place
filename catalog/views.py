from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .forms import ProductForm, ProductModeratorForm



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
    def form_valid(self, form):
        # Перед сохранением присваиваем текущего пользователя
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = self.request.user
        # Проверяем, если пользователь - владелец или модератор
        if user != self.object.owner and not user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'




