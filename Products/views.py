from django.shortcuts import render, redirect
from .models import Product, Category , Review
from .serializers import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status   # status code
from rest_framework.viewsets import ModelViewSet # eita use korle get, post, put, delete sob kaj kora jabe ak sathe. (short api view)
from rest_framework.permissions import IsAuthenticated # user must be authenticated to access the API
# custom permission
from .permissions import CustomPermission #


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
            review = Review.objects.get(product = id)
            # review = Review.objects.get(product = Product.objects.get(id = id))
        except Review.DoesNotExist:
            review = None
        context = {
            'review': review,
            'product': Product.objects.get(id = id)
        }

    return render(request, 'product_review.html', context)

# API view --------------------------------------------------------------------------------------------------------------------------------------
class CategoryAPIView(APIView):
    # Get
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True) # many = True dile multiple data return korbe jeson format e. model theke data nicchi (get)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def get(self, request, id):
        categories = Category.objects.get(id = id)
        serializer = CategorySerializer(categories)
        return Response(serializer.data, status = status.HTTP_200_OK)

    # Post
    def post(self, request):
        serializer = CategorySerializer(data = request.data) # data = request.data dile json data a serialize korbe , request.data হলো ক্লায়েন্ট থেকে পাঠানো ডেটা, যা JSON ফরম্যাটে থাকে। এই ডেটা CategorySerializer-এ পাস করা হয়।. user er kach theke data nicchi(post)
        if serializer.is_valid(): # is_valid() মেথডটি দেখে যাচ্ছে যে ডেটা ভ্যালিড হয়েছে কিনা। যদি হয় তাহলে সেভ করা হবে।
            serializer.save() # এই মেথডটি ভ্যালিড ডেটা ডেটাবেসে সেভ করে। অর্থাৎ, নতুন একটি ক্যাটাগরি তৈরি হয়।
            return Response(serializer.data, status = status.HTTP_201_CREATED) # এখানে serializer.data হলো সেভ হওয়া ডেটা যা ক্লায়েন্ট পাঠানো হয়েছে। এই ডেটা ক্লায়েন্ট পাঠানো হবে।
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CategoryDetailAPIView(APIView):
    # Get, when user find not existing data
    def get(self, request, id):
        try:
            category = Category.objects.get(id = id)
        except Category.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status = status.HTTP_200_OK)

    # Same logic in if condision, tobe try except use kora vlo
    # def get (self, request, id):
    #     if Category.objects.filter(id = id).exists():
    #         category = Category.objects.get(id = id)
    #         serializer = CategorySerializer(category)
    #         return Response(serializer.data, status = status.HTTP_200_OK)
    #     return Response(status = status.HTTP_404_NOT_FOUND)


    # Put
    def put(self, request, id):
        try:
            category = Category.objects.get(id = id)
        except Category.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data = request.data) # put er jonno get and post a ja use korchi duita e dite hobe (get.category, post.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    # put in if condition
    # def put(self, request, id):
    #     if Category.objects.filter(id = id).exists():
    #         category = Category.objects.get(id = id)
    #         serializer = CategorySerializer(category, data = request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status = status.HTTP_200_OK)
    #         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    #     return Response(status = status.HTTP_404_NOT_FOUND)

    # Delete
    def delete(self, request, id):
        try:
            category = Category.objects.get(id = id)
        except Category.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    # delete in if condition
    # def delete(self, request, id):
    #     if Category.objects.filter(id = id).exists():
    #         category = Category.objects.get(id = id)
    #         category.delete()
    #         return Response(status = status.HTTP_204_NO_CONTENT)
    #     return Response(status = status.HTTP_404_NOT_FOUND)


# API in shortly way for 3 line --------------------------------------------------------------------------------------------------------------------------------------
# class CategoryViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# Authentication in Rest_framework --------------------------------------------------------------------------------------------------------------------------------------
# Token based authentication
# User give username and password, then server give token. Then user give token to server and server give data to user.
# How is the token generated?
# The JWT token is generated by the server and sent to the client. The client sends the token back to the server for every request. The server verifies the token and sends the response.
# The server uses the secret key to generate the token. The secret key is used to sign the token. The server uses the secret key to verify the token.
# JWT takes the user object and the secret key as input and generates a token. The token is sent to the client. The client sends the token back to the server for every request. The server verifies the token and sends the response.
# the token is generated by encoding the user object and the secret key. The token is sent to the client. The client sends the token back to the server for every request. The server verifies the token and sends the response.
# the token returned to the user is generated by encoding the user object and the secret key. The token is sent to the client. The client sends the token back to the server for every request. The server verifies the token and sends the response.

# API authontication classification
# 1. No authentication -> anyone can access the API
# 2. Basic authentication -> username and password
# 3. Token based authorization -> private API -> only authenticated user can access the API
# 4. Authorization based on roles -> admin, user, manager

# Token based authentication. 3. Token based authorization -> private API -> only authenticated user can access the API
# class CategoryViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsAuthenticated] # user must be authenticated to access the API

# Custom permission
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermission] # use custom permission, user must be authenticated and superuser to access the API

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().list(request, *args, **kwargs)
        return Response(status = status.HTTP_401_UNAUTHORIZED)