from django.shortcuts import render

# Create your views here.
def UserLogin(request):
    return render(request, 'userlogin.html')