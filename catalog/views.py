from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category
from django.http import HttpResponse

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

def add_product(request):

    if request.method == 'POST':
        name_product = request.POST.get('name_product')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        category = Category.objects.get(id=category_id)
        product = Product(
            name_product=name_product,
            category=category,
            description=description,
            price=price,
            image=image,
        )

        product.save()
        response = f"Товар {name_product} успешно добавлен! <a href='/'>Вернуться на главную</a>"
        return HttpResponse(response)
    category = Category.objects.all()
    return render(request, 'catalog/add_product.html', {'categories': category})


def add_category(request):

    if request.method == "POST":
        name_category = request.POST.get('name_category')
        description = request.POST.get("description")

        category = Category(
            name_category = name_category,
            description = description
        )

        category.save()
        return HttpResponse(f"Категория {name_category} успешно добавлена! <a href='/'>Вернуться на главную</a>")
    return render(request, 'catalog/add_category.html')