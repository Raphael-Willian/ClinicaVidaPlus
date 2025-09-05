from django import forms
from .models import PacientesCadastrados

class PacienteForm(forms.ModelForm):
    class Meta:
        model = PacientesCadastrados
        fields = ["nome_completo", "idade", "telefone", "rg", "cpf"]
        widgets = {
            'nome_completo': forms.TextInput(attrs={'id': 'id_nome', 'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'id': 'id_idade', 'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'id': 'id_telefone', 'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'id': 'id_rg', 'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'id': 'id_cpf', 'class': 'form-control'}),
        }