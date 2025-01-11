from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        #user = request.user
        product = Product.objects.get(id = id)
        review_text = request.POST.get('review_text')
        rating = request.POST.get('rating')
        review = Review(product = product, review_text = review_text, rating = rating)
        review.save()
        return redirect('product_review', id = id)
    
    if request.method == 'GET':
        try:
            review = Review.objects.get(product = id) # product = id dilam keno?
            # review = Review.objects.get(product = Product.objects.get(id = id))
        except Review.DoesNotExist:
            review = None
        context = {
            'review': review,
            'product': Product.objects.get(id = id)
        }
    
    return render(request, 'product_review.html', context)