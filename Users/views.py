from django.shortcuts import render, redirect
from Users.models import CustomUser
from Home.views import home
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username') # Get the username from the form
        password = request.POST.get('password') # Get the password from the form
        user = authenticate(request, username=username, password=password) # Check if the user is valid
        if user is not None:
            login(request, user)
            return redirect('home') # Redirect to the home page
        return render(request, 'userlogin.html', {'error': 'Invalid credentials'})
    return render(request, 'userlogin.html')