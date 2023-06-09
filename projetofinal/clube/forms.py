from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Atleta, Jogo, Treino, Voto_treino


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)


class AtletaForm(forms.ModelForm):
    equipa = forms.ChoiceField(choices=[('Infantis M', 'Infantis M'), ('Infantis F', 'Infantis F'),
                                        ('Iniciados M', 'Iniciados M'), ('Iniciadas F', 'Iniciadas F'),
                                        ('Cadetes M', 'Cadetes M'), ('Cadetes F', 'Cadetes F'),
                                        ('Juvenis M', 'Juvenis M'), ('Juvenis F', 'Juvenis F'),
                                        ('Juniores M', 'Juniores M'), ('Juniores F', 'Juniores F')], required=True)
    num_tel = forms.IntegerField(required=True)
    data_nascimento = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'}))
    sexo = forms.ChoiceField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], required=True)

    class Meta:
        model = Atleta
        fields = ['equipa', 'num_tel', 'data_nascimento', 'sexo']

class TreinadorForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    equipa = forms.ChoiceField(choices=[('M', 'Infantis M'), ('F', 'Infantis F'), ('M', 'Iniciados M'),
                                        ('F', 'Iniciadas F'), ('M', 'Cadetes M'), ('F', 'Cadetes F'),
                                        ('M', 'Juvenis M'), ('F', 'Juvenis F'),
                                        ('M', 'Juniores M'), ('F', 'Juniores F')], required=True)
    num_tele = forms.CharField(max_length=20, required=True)
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'equipa', 'num_tele')

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['jogo_local', 'jogo_data', 'jogo_hora']
        widgets = {
            'jogo_data': forms.DateInput(attrs={'type': 'date'}),
            'jogo_hora': forms.TimeInput(attrs={'type': 'time'}),
        }

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['treino_local', 'treino_data', 'treino_hora']
        widgets = {
            'treino_data': forms.DateInput(attrs={'type': 'date'}),
            'treino_hora': forms.TimeInput(attrs={'type': 'time'}),
        }

class VotoTreinoForm(forms.ModelForm):
    class Meta:
        model = Voto_treino
        fields = ['vai_treinar', 'justificacao']
        labels = {
            'vai_treinar': 'Disponível para o treino?',
            'justificacao': 'Justificação (caso não disponível)',
        }
