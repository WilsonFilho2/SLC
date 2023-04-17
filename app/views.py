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
    produtos = models.Produtos.objects.all()
    return render(request, 'app/index.html',{
        'listas': listas,
        'produtos': produtos
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


def cadastrar_produtos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = float(request.POST.get('preco'))

        produto = models.Produtos.objects.create(nome=nome, preco=preco)
        produto.save()

        return redirect('index')
    
    return redirect('index')

    


def cadastrar_lista(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        lista = models.Lista.objects.create(nome=nome)
        lista.save()
        return redirect('index')

    return redirect('index')


def adicionar_produtos(request, lista_id):
    if request.method == 'POST':
        lista = models.Lista.objects.get(id=lista_id)
        produto_id = int(request.POST.get('produtos'))
        produto = models.Produtos.objects.get(id=produto_id)
        produto.lista.add(lista)

    lista = models.Lista.objects.get(id=lista_id)
    nao_produto = models.Produtos.objects.exclude(lista=lista).all()
    produtos = lista.produtos.all()
    total = 0

    for produto in produtos:
        total += float(produto.preco)

    return render(request, 'app/lista.html', {
        'lista': lista,
        'nao_produto': nao_produto,
        'produtos': produtos,
        'total': total,
    })