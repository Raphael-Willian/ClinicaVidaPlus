# consultas/forms.py
from django import forms
from .models import Consulta


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ["profissional", "data", "hora_inicio", "hora_do_fim", "observacoes"]
        widgets = {
            'profissional': forms.Select(attrs={'id': 'id_profissional', 'class': 'form-control'}),
            'data': forms.DateInput(attrs={'type': 'date', 'id': 'id_data', 'class': 'form-control'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time', 'id': 'id_hora_inicio', 'class': 'form-control'}),
            'hora_fim': forms.TimeInput(attrs={'type': 'time', 'id': 'id_hora_fim', 'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
