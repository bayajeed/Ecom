from django.urls import path
from .views import UserLogin

urlpatterns = [
    path('users/', UserLogin, name = 'UserLogin')
]