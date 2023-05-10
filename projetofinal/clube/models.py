from datetime import timezone, datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Utilizador(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    equipa = models.CharField(max_length=50)
    num_tel = models.IntegerField(unique=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=10)
class Atleta(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    equipa = models.CharField(max_length=50)
    num_tel = models.IntegerField(unique=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=10)


    def __str__(self):
        return self.user.username

class Treinador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    equipa = models.CharField(max_length=50)
    num_tel = models.IntegerField(unique=True)

class Diretor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_tel = models.IntegerField(unique=True)


class Treino(models.Model):
    treino_data = models.DateField(default=False)
    treino_hora = models.TimeField(default=False)
    treino_local = models.CharField(max_length=200)

class Opcao_treino(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    opcao_treino = models.CharField(max_length=20)
    presencas = models.IntegerField(default=0)

class Voto_treino(models.Model):
    jogador = models.ForeignKey(User, on_delete=models.CASCADE)
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE, null=True)
    justificacao = models.CharField(max_length=200, blank=True)
    vai_treinar = models.BooleanField(default=True)

class Jogo(models.Model):
    jogo_data = models.DateField('data')
    jogo_hora = models.TimeField()
    jogo_local = models.CharField(max_length=200)

class Opcao_jogo(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    opcao_jogo = models.CharField(max_length=20)
    presencas = models.IntegerField(default=0)