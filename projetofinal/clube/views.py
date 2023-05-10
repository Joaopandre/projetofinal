from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm, AtletaForm, TreinadorForm, DiretorForm, JogoForm
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import context
from django.urls import reverse
from .models import Atleta, Jogo, Voto_jogo


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

def registar(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('clube:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'clube/registar.html', {'form': form})

def registar_atleta(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        atleta_form = AtletaForm(request.POST)
        if user_form.is_valid() and atleta_form.is_valid():
            user = user_form.save(commit=False)
            user.email = user_form.cleaned_data['email']
            user.save()
            atleta = atleta_form.save(commit=False)
            atleta.user = user
            atleta.save()
            return redirect('sucesso')
    else:
        user_form = CustomUserCreationForm()
        atleta_form = AtletaForm()
    return render(request, 'clube/registar_atleta.html', {'user_form': user_form, 'atleta_form': atleta_form})




def registar_treinador(request):
    if request.method == 'POST':
        form = TreinadorForm(request.POST)
        if form.is_valid():
            treinador = form.save()
            login(request, treinador)
            return redirect('clube:home')
    else:
        form = TreinadorForm()
    return render(request, 'clube/registar_treinador.html', {'form': form})

def registar_diretor(request):
    if request.method == 'POST':
        form = DiretorForm(request.POST)
        if form.is_valid():
            diretor = form.save()
            login(request, diretor)
            return redirect('clube:criar_jogo')
    else:
        form = DiretorForm()
    return render(request, 'clube/registar_diretor.html', {'form': form})

def historia(request):
    return render(request, 'clube/historia.html')

@login_required
def criar_jogo(request):
    if request.method == 'POST':
        form = JogoForm(request.POST)
        if form.is_valid():
            jogo = form.save(commit=False)
            jogo.criador = request.user
            jogo.save()
            form.save_m2m()
            return redirect('clube:home')
    else:
        form = JogoForm()
    return render(request, 'clube/criar_jogo.html', {'form': form})

@login_required
def jogos(request):
    jogos_criados = Jogo.objects.filter(criador=request.user)
    jogos_participantes = request.user.jogos.all()
    jogador_vai_jogar = {}
    for jogo in jogos_participantes:
        votacao = Voto_jogo.objects.filter(jogador=request.user, jogo=jogo).first()
        if votacao:
            jogador_vai_jogar[jogo.id] = votacao.vai_jogar
        else:
            jogador_vai_jogar[jogo.id] = None
    return render(request, 'clube/jogo.html', {'jogos_criados': jogos_criados, 'jogos_participantes': jogos_participantes, 'jogador_vai_jogar': jogador_vai_jogar})

@login_required
def voto_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, id=jogo_id)
    voto = Voto_jogo.objects.filter(user=request.user, jogo=jogo).first()

    if request.method == 'POST':
        vai_ao_jogo = request.POST.get('vai_ao_jogo') == 'True'

        if voto:
            voto.vai_ao_jogo = vai_ao_jogo
            voto.save()
        else:
            voto = Voto_jogo(user=request.user, jogo=jogo, vai_ao_jogo=vai_ao_jogo)
            voto.save()

        return HttpResponseRedirect(reverse('clube:home'))

    return render(request, 'clube/voto_jogo.html', {'jogo': jogo, 'voto': voto})