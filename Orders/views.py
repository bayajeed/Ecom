from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import Cart,CartItem


def CartView(request):
    print('testtttttttttttttt',request.user)
    if not request.user.is_authenticated:
        return redirect('signin')
    user = request.user
    cart = Cart.objects.filter(user = user).first()
    print(cart)
    if not cart:
        cart = Cart.objects.create(user = user)
    cart_items = Cart.products.through.objects.filter(cart = cart)
    contex = {
        'cart_items': cart_items,
        'cart': cart
    }
    return render(request, 'cart.html', contex)

