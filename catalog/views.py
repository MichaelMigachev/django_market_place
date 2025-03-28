from django.shortcuts import render, get_object_or_404
from catalog.models import Product

# def home(request):
#     return render(request, 'catalog/base.html')

def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/products_list.html', context)


def product (request, pk):
    product = get_object_or_404(Product, id=pk)
    context = {"product": product}
    return render(request, 'catalog/product.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')
