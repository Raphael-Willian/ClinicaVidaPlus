from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PacientesCadastrados

class RegistroForm(UserCreationForm):
    nome_completo = forms.CharField(max_length=120, required=True)
    idade = forms.IntegerField(required=False)
    telefone = forms.CharField(max_length=16, required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "nome_completo", "idade", "telefone"]