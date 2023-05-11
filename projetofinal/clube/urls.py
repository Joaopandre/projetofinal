from django.urls import path
from . import views

app_name = 'clube'

urlpatterns = [
    path('', views.home, name='home'),

    path('registar', views.registar, name='registar'),
    path('atleta', views.registar_atleta, name='registar_atleta'),
    path('treinador', views.registar_treinador, name='registar_treinador'),


    path('historia/', views.historia, name='historia'),

    path('jogos/', views.jogos, name='jogos'),
    path('criar_jogo/', views.criar_jogo, name='criar_jogo'),
    path('<int:jogo_id>/', views.detalhe_jogo, name='detalhe_jogo'),

    path('treinos/', views.treinos, name='treinos'),
    path('criar_treino/', views.criar_treino, name='criar_treino'),
    path('<int:treino_id>/', views.detalhe_treino, name='detalhe_treino'),

    path('fazerlogin', views.fazerlogin, name='fazerlogin'),
    path('fazerlogout', views.fazerlogout, name='fazerlogout'),

    path('users/', views.lista_users, name='lista_users'),

]
