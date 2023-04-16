from django.db import models

# Create your models here.


class Lista(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.id}: {self.nome}"


class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    lista = models.ManyToManyField(Lista, blank=True, related_name="produtos")

    def __str__(self) -> str:
        return f"{self.id}: {self.nome}"
