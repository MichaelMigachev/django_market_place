from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductListView, ContactsView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, CategoryProductsView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/', cache_page(60*10)(ProductDetailView.as_view()), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/contacts/', ContactsView.as_view(), name='contacts'),

    path('category/<int:category_id>/', CategoryProductsView.as_view(), name='category_products'),

]


# ProductUpdateView