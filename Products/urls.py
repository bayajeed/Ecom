from django.urls import path
from .views import *

urlpatterns = [
    path('products/', all_products, name = 'all_products'),
    path('product/<int:id>/', product_detail, name = 'product_detail'),
    path('product/review/<int:id>', product_review, name = 'product_review'),
]