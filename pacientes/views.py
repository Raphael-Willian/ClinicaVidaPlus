from django.shortcuts import render
from .models import PacientesCadastrados
from django.db.models import Avg


def total_de_pacientes(request):
    if request.method == 'GET':
        lista_de_pacientes = PacientesCadastrados.objects.all() #lista todos os dados da tabela
        media_idades = PacientesCadastrados.objects.aggregate(Avg('idade'))['idade__avg']
        numero_de_pacientes = lista_de_pacientes.count()

        paciente_mais_velho = PacientesCadastrados.objects.order_by('-idade').first()
        paciente_mais_novo = PacientesCadastrados.objects.order_by('idade').first()

        query = request.GET.get('q')
        if query:
            pacientes = PacientesCadastrados.objects.filter(nome_completo__icontains=query)

        else:
            pacientes = PacientesCadastrados.objects.all()

        return render(request, "pacientes.html", {
            "lista_de_pacientes": lista_de_pacientes,
            "total": numero_de_pacientes,
            "media_idades":media_idades,
            "paciente_mais_velho":paciente_mais_velho,
            "paciente_mais_novo":paciente_mais_novo,
            "pacientes":pacientes,
            "query":query
        })

