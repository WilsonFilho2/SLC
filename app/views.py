from django.shortcuts import render, redirect
from django.http import request
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from . import models


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    listas = models.Lista.objects.all()
    return render(request, 'app/index.html',{
        'listas': listas
    })


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




#####################################################################################################


def cadastro_produtos(request, lista_id):
    return render(request, 'app/lista.html', {
        'lista': lista_id
    })


def cadastrar_lista(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        lista = models.Lista.objects.create(nome=nome)
        lista.save()
        return redirect('index')

    return redirect('index')
