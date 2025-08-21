from django.shortcuts import render
from .models import PacientesCadastrados


def total_de_pacientes(request):
    if request.method == 'GET':
        lista_de_pacientes = PacientesCadastrados.objects.all() #lista todos os dados da tabela
        return render(request, "pacientes.html", {"pacientes": lista_de_pacientes})


