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
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            django_login(request, user=user)
            return redirect('index')
        
        else:
            return render(request, 'app/login.html', {
                'message': 'Usuário Não existente',
            })


    return render(request, 'app/login.html')


def logout(request):
    django_logout(request)
    return render(request, 'app/login.html', {
        'message': "Log out",
    })


def cadastro(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try: # se fer erro, é porque já existe
            user = authenticate(username=username, email=email, password=password)
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            user = authenticate(username=username, email=email, password=password)
            django_login(request, user=user)
            return redirect('index')
        
        except:
            return render(request, 'app/cadastro.html',{
                'message': 'Usuário Inválido ou Já existente'
            })        
        

    return render(request, 'app/cadastro.html')
