from django.urls import path
from .views import CartView 

urlpatterns = [
    path('cart/', CartView, name = 'cart'),

]