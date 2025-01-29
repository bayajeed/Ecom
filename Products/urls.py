from django.urls import path
from .views import *

urlpatterns = [
    path('products/', all_products, name = 'all_products'), # name ke kothay call korbe? 
    path('product/<int:id>/', product_detail, name = 'product_detail'),
    path('product/review/<int:id>', product_review, name = 'product_review'),
    path('categories/', CategoryAPIView.as_view(), name = 'api_categories'), 
]
