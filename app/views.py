from django.shortcuts import render, redirect
from django.http import request
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'app/index.html')


def login(request):
    if request.method == 'POST':
        pass
    return render(request, 'app/login.html')


def logout(request):
    pass


def cadastro(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

    return render(request, 'app/cadastro.html')