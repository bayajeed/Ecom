from django.shortcuts import render
from .models import Product, Category


# Create your views here.

def all_products(request):
    all_products = Product.objects.all()
    # for product in all_products:
    #     print("*"*50)
    #     print("product ID:" , product.id)
    #     print("name:", product.name)
    #     print("price:", product.price)
    #     print(product.description)
    #     print("*"*50)

    context = {
        'products': all_products
    }
    return render(request, 'all_products.html', context)

def product_detail(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist:
        product = None
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

