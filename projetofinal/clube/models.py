from datetime import timezone, datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


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
    local_treino = models.CharField(max_length=50)
    data_treino = models.DateTimeField('Data de Treino: ')



class Opcao_treino(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    opcao_treino = models.CharField(max_length=20)
    presencas = models.IntegerField(default=0)


class Jogo(models.Model):
    data = models.DateField('data')
    hora = models.TimeField()
    local = models.CharField(max_length=200)
    jogadores = models.ManyToManyField(User, through='Voto_jogo')


class Voto_jogo(models.Model):
    jogador = models.ForeignKey(User, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    vai_jogar = models.BooleanField()