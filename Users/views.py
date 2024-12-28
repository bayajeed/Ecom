from django.shortcuts import render

# Create your views here.
def UserLogin(request):
    return render(request, 'index.html', name = 'UserLogin')