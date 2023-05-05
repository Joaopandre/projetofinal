from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import context
from django.urls import reverse



def home(request):
    context = {}
    return render(request, 'clube/home.html', context)

def is_admin(user):
    return user.is_authenticated and user.is_superuser

def fazerlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('clube:home')
        else:
            context = {'msg_erro': 'Credenciais inválidas'}
            return render(request, 'clube/fazerlogin.html', context)
    else:
        return render(request, 'clube/fazerlogin.html')


@login_required
def fazerlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('clube:home'))

