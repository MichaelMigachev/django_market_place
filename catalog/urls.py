from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('product/<int:pk>/', views.product, name='product'),
    path('contacts/', views.contacts, name='contacts'),
    path('add_product/', views.add_product, name="add_product"),
    path('add_category/', views.add_category, name="add_category"),
]
