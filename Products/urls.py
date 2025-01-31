from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter # eita use korle get, post, put, delete sob kaj kora jabe ak sathe. (short api view)

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename = 'categories') # basename = 'categories' ki kaj kore? eita category viewset er name ta category viewset er url e path banay. e.g: http://

urlpatterns = [
    path('products', all_products, name = 'all_products'), # name ke kothay call korbe? 
    path('product/<int:id>', product_detail, name = 'product_detail'),
    path('product/review/<int:id>', product_review, name = 'product_review'),
    # for Get API
    path('api/categories/<int:id>', CategoryAPIView.as_view(), name = 'api_category'), # name = 'api_category' ki kaj kore?  
    path('api/categories', CategoryAPIView.as_view(), name = 'api_categories'),
    # For Post API
    path('api/CategoryDetailAPIView/<int:id>', CategoryDetailAPIView.as_view(), name = 'CategoryDetail')

    
] + router.urls