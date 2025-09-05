from django.shortcuts import render, redirect
from .models import Consulta
from .forms import ConsultaForm
from django.contrib import messages
from pacientes.forms import PacienteForm

def cadastro_consulta(request):
    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST)
        consulta_form = ConsultaForm(request.POST)

        if paciente_form.is_valid() and consulta_form.is_valid():
            paciente = paciente_form.save()
            consulta = consulta_form.save(commit=False)
            consulta.paciente = paciente
            consulta.save()
            return redirect('confirmacao')
    else:
        paciente_form = PacienteForm()
        consulta_form = ConsultaForm()

    return render(request, 'blog.html', {
        'paciente_form': paciente_form,
        'consulta_form': consulta_form
    })

def confirmacao(request):
    return render(request, 'consultas/confirmacao.html')
