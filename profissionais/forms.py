from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profissional

class ProfissionalCreationForm(UserCreationForm):
    class Meta:
        model = Profissional
        fields = '__all__'  # ou liste os campos que você quiser

class ProfissionalChangeForm(UserChangeForm):
    class Meta:
        model = Profissional
        fields = '__all__'
