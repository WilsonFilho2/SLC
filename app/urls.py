from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('lista', views.cadastrar_lista, name="lista"),
    path('produto', views.cadastrar_produtos, name="produto"),
    path('<int:lista_id>', views.adicionar_produtos, name="addproduto")
]
