from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class Corretor(models.Model):
    nome = models.CharField(
        max_length=255
    )
    creci = models.CharField(
        max_length=50, unique=True
    )
    telefone = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.nome


class Imovel(models.Model):
    titulo = models.CharField(
        max_length=255
    )
    descricao = models.TextField()
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    foto_principal = models.ImageField(upload_to='imoveis/')
    disponivel = models.BooleanField(default=True)
    corretor = models.ForeignKey(Corretor, on_delete=models.CASCADE)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

    def calcular_comissao(self):
        if self.preco:
            return float(self.preco) * 0.05
        return 0.00
