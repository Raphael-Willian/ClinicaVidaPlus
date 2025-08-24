from django import forms
from .models import PacientesCadastrados

class PacienteForm(forms.ModelForm):
    class Meta:
        model = PacientesCadastrados
        fields = ["nome_completo", "idade", "telefone"]
