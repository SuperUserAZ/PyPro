from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def signup(request):
    return render(request, 'main/signup.html')

def login(request):
    return render(request, 'main/login.html')


