from datetime import timezone, datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Atleta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    disponibilidade = models.BooleanField(default=False)
    escalão = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    num_tel = models.IntegerField(unique=True)

class Treinador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    escalão = models.CharField(max_length=50)
    num_tel = models.IntegerField(unique=True)


class Diretor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_tel = models.IntegerField(unique=True)


class Treino(models.Model):
    local_treino = models.CharField(max_length=50)
    data_treino = models.DateTimeField('data de treino')

class Jogo(models.Model):
    local_jogo = models.CharField(max_length=50)
    data_jogo = models.DateTimeField('data do jogo')

class Opcao_treino(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    opcao_treino = models.CharField(max_length=20)
    presencas = models.IntegerField(default=0)


class Opcao_jogo(models.Model):
    jogo = models.ForeignKey(Treino, on_delete=models.CASCADE)
    opcao_jogo = models.CharField(max_length=20)
    presencas = models.IntegerField(default=0)