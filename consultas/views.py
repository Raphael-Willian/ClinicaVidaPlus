from django.shortcuts import render, redirect
from .models import Consulta
from .forms import ConsultaForm
from django.contrib import messages
from pacientes.forms import PacienteForm
from pacientes.models import PacientesCadastrados

def cadastro_consulta(request):
    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST)
        consulta_form = ConsultaForm(request.POST)

        if paciente_form.is_valid() and consulta_form.is_valid():
            profissional = consulta_form.cleaned_data['profissional']
            cpf = paciente_form.cleaned_data['cpf']

            # ⚠️ Tenta encontrar paciente existente
            try:
                paciente = PacientesCadastrados.objects.get(cpf=cpf)
                print("Paciente já existe:", paciente)
            except PacientesCadastrados.DoesNotExist:
                paciente = paciente_form.save(commit=False)
                paciente.profissional = profissional
                paciente.save()
                print("Paciente criado:", paciente)

            # Cria a consulta e associa ao paciente
            consulta = consulta_form.save(commit=False)
            consulta.pacientes = paciente
            consulta.save()

            print("Consulta salva com sucesso:", consulta)
            return redirect('confirmacao_command')

        else:
            print("Formulários inválidos:")
            print("Paciente form errors:", paciente_form.errors)
            print("Consulta form errors:", consulta_form.errors)

    else:
        paciente_form = PacienteForm()
        consulta_form = ConsultaForm()

    return render(request, 'blog.html', {
        'paciente_form': paciente_form,
        'consulta_form': consulta_form,
        'mostrar_consulta': request.method == 'POST'
    })



def confirmacao(request):
    return render(request, 'consultas/confirmacao.html')
