from django.urls import path
from . import views

app_name = 'clube'

urlpatterns = [
    path('', views.home, name='home'),

    path('fazerlogin', views.fazerlogin, name='fazerlogin'),
    path('fazerlogout', views.fazerlogout, name='fazerlogout'),









]