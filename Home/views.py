from django.shortcuts import render

# Create your views here.
def home(request):
    print(request.user) # user kotha theke linkup hoilo? 
    return render(request, 'index.html')