from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profissional
from django import forms

class ProfissionalCreationForm(UserCreationForm):
    class Meta:
        model = Profissional
        fields = '__all__'  # ou liste os campos que você quiser

class ProfissionalChangeForm(UserChangeForm):
    class Meta:
        model = Profissional
        fields = '__all__'

class ProfissionalUpdateForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = [
            'nome_completo',
            'email', 'telefone',
            'especialidade','nascimento',
            'cpf',
            'genero',
            'endereco',
            'cep',
            'registro_profissional',
            'status'
        ]

