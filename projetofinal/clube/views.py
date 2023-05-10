from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, AtletaForm, TreinadorForm, DiretorForm, JogoForm, TreinoForm, VotoTreinoForm
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import context
from django.urls import reverse
from .models import Atleta, Jogo, Treino, Voto_treino, Opcao_treino


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
            return redirect('clube:home')
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
    jogos_criados = Jogo.objects.filter()
    context = {'jogos_criados': jogos_criados}
    return render(request, 'clube/home.html', context)

@login_required
def detalhe_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, id=jogo_id)
    context = {'jogo': jogo}
    return render(request, 'clube/detalhe_jogo.html', context)

@login_required
def treinos(request):
    treinos_criados = Treino.objects.filter()
    context = {'treinos_criados': treinos_criados}
    return render(request, 'clube/home.html', context)


@login_required
def voto_treino(request, id_treino):
    treino = get_object_or_404(Treino, id=id_treino)

    if not treino.is_ativo:
        messages.warning(request, 'Esse treino não está mais ativo.')
        return redirect('clube:treinos')

    participando = Voto_treino.objects.filter(treino=treino, jogador=request.user).exists()

    if request.method == 'POST':
        form = VotoTreinoForm(request.POST)
        if form.is_valid():
            vai_treinar = form.cleaned_data['vai_treinar']
            justificacao = form.cleaned_data['justificacao']
            if not participando:
                voto = Voto_treino(treino=treino, jogador=request.user, vai_treinar=vai_treinar, justificacao=justificacao)
                voto.save()
                messages.success(request, 'Voto registrado com sucesso.')
            else:
                messages.warning(request, 'Você já votou neste treino.')
            return redirect('clube:detalhe_treino', treino_id=id_treino)
        else:
            messages.error(request, 'O formulário contém erros. Verifique os campos abaixo.')
    else:
        form = VotoTreinoForm()

    return render(request, 'clube/_treino.html', {'treino': treino, 'participando': participando, 'form': form})


@login_required
def detalhe_treino(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id)
    opcoes_treino = Opcao_treino.objects.filter(treino_id=treino.id)
    participando = Voto_treino.objects.filter(jogador=request.user, treino=treino).exists()
    context = {'treino': treino, 'opcoes_treino': opcoes_treino, 'participando': participando}
    return render(request, 'clube/detalhe_treino.html', context)

@login_required
def criar_treino(request):
    if request.method == 'POST':
        form = TreinoForm(request.POST)
        if form.is_valid():
            treino = form.save(commit=False)
            treino.criador = request.user
            treino.save()
            form.save_m2m()
            return redirect('clube:home')
    else:
        form = TreinoForm()
    return render(request, 'clube/criar_treino.html', {'form': form})



@login_required
def lista_users(request):
    users = User.objects.all()
    return render(request, 'clube/lista_users.html', {'users': users})