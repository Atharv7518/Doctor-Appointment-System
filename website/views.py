from django.shortcuts import render

def landing(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, 'home.html')

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')

def under_development(request):
    return render(request, 'under_development.html')