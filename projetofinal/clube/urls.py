from django.urls import path
from . import views

app_name = 'clube'

urlpatterns = [
    path('', views.home, name='home'),

    path('registar', views.registar, name='registar'),
    path('atleta', views.registar_atleta, name='registar_atleta'),
    path('treinador', views.registar_treinador, name='registar_treinador'),
    path('diretor', views.registar_diretor, name='registar_diretor'),

    path('historia/', views.historia, name='historia'),

    path('jogos/', views.jogos, name='jogos'),
    path('criar_jogo/', views.criar_jogo, name='criar_jogo'),
    path('voto_jogo/<int:jogo_id>/', views.voto_jogo, name='voto_jogo'),



    path('fazerlogin', views.fazerlogin, name='fazerlogin'),
    path('fazerlogout', views.fazerlogout, name='fazerlogout'),

]
