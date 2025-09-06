from django.contrib import admin
from .models import PacientesCadastrados

@admin.register(PacientesCadastrados)
class PacientesCadastradosAdmin(admin.ModelAdmin):
    fields = ('nome_completo', 'idade', 'telefone', 'rg', 'cpf')
    list_display = ('nome_completo', 'idade', 'telefone', 'rg', 'cpf')

