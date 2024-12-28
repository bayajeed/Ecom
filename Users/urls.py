from django.urls import path
from .views import UserLogin

urlpatterns = [
    path('', UserLogin, name = 'UserLogin'),
]