from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from catalog.services import get_products_by_category, get_products_by_category_from_cache, get_products_from_cache



class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_products_from_cache()
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


class CategoryProductsView(LoginRequiredMixin, ListView):
    template_name = 'catalog/category_products.html'
    context_object_name = 'products'

    def setup(self, request, *args, **kwargs):
        """Инициализация атрибутов перед обработкой запроса"""
        super().setup(request, *args, **kwargs)
        self.category = get_object_or_404(Category, id=kwargs['category_id'])

    def get_queryset(self):
        """Получаем продукты категории с кешированием"""
        return get_products_by_category_from_cache(self.category.id)

    def get_context_data(self, **kwargs):
        """Добавляем категорию в контекст"""
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context