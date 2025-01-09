from django.shortcuts import render
from .models import Product, Category , Review


# Create your views here.

def all_products(request):
    all_products = Product.objects.all()
    for product in all_products:
        print(product.id)
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

def product_review(request, id):
    try:
        review = Review.objects.get(id = id)
    except Review.DoesNotExist:
        review = None
    context = {
        'review' : review
    }
    return render(request, 'product_review.html', context)
