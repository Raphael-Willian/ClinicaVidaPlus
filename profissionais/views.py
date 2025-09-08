from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from pacientes.models import PacientesCadastrados
from django.db.models import Avg
from pacientes.forms import PacienteForm
from consultas.forms import ConsultaForm, ConsultaEditarForm
from django.contrib import messages
from consultas.models import Consulta
from profissionais.models import Profissional
from .forms import ProfissionalUpdateForm


@login_required(login_url="login_command")
def consulta_profissional(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Consulta agendada com sucesso!")
                return redirect("consulta_profissional_command")
            except Exception as e:
                messages.error(request, f"Erro ao salvar consulta: {e}")
    else:
        form = ConsultaForm();

    consultas = Consulta.objects.all().order_by('data', 'hora_inicio')
    pacientes = PacientesCadastrados.objects.all()
    profissionais = Profissional.objects.all()

    context = {
        'form': form,
        'consultas': consultas,
        'pacientes': pacientes,
        'profissionais': profissionais,
    }

    return render(request, 'consultapro.html', context)


@login_required(login_url="login_command")
def total_de_pacientes(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.profissional = request.user
            paciente.save()
            return redirect("total_de_pacientes_command")
    else:
        form = PacienteForm()

    lista_de_pacientes = PacientesCadastrados.objects.filter(profissional=request.user)
    media_idades = lista_de_pacientes.aggregate(Avg("idade"))["idade__avg"]
    numero_de_pacientes = lista_de_pacientes.count()
    paciente_mais_velho = lista_de_pacientes.order_by("-idade").first()
    paciente_mais_novo = lista_de_pacientes.order_by("idade").first()

    query = request.GET.get("q")
    if query:
        pacientes = lista_de_pacientes.filter(nome_completo__icontains=query)
    else:
        pacientes = lista_de_pacientes

    return render(request, "pacientes.html", {
        "lista_de_pacientes": lista_de_pacientes,
        "total": numero_de_pacientes,
        "media_idades": media_idades,
        "paciente_mais_velho": paciente_mais_velho,
        "paciente_mais_novo": paciente_mais_novo,
        "pacientes": pacientes,
        "query": query,
        "form": form
    })

@login_required(login_url="login_command")
def configuracoes(request):
    profissional = request.user

    if request.method == 'POST':
        form = ProfissionalUpdateForm(request.POST, instance=profissional)
        if form.is_valid():
            form.save()
            messages.success(request, "Alteração consluída com sucesso!")
            return redirect('configuracoes')

        else:
            messages.error(request, "Erro ao realizar a alteração.")

    else:
        form = ProfissionalUpdateForm(instance=profissional)

    return render(request, 'configuracoes.html', {'form': form})

@login_required(login_url="login_command")
def editar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    form = ConsultaEditarForm(request.POST or None, instance=consulta)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('consulta_profissional_command')

    return render(request, 'editar_consulta.html', {'form': form})

@login_required(login_url="login_command")
def remover_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    if request.method == 'POST':
        consulta.delete()
        return redirect('consultas')


def login_profissional(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("total_de_pacientes_command")
        else:
            return render(request, "login.html", {"error": "Email ou senha inválidos"})
    return render(request, "login.html")


@login_required
def dashboard(request):
    profissional = request.user  # pega o profissional logado

    # aqui você pode puxar dados relacionados, ex:
    consultas = Consulta.objects.filter(profissional=profissional)
    total_consultas = consultas.count()

    context = {
        'profissional': profissional,
        'consultas': consultas,

        'total_consultas': total_consultas,
    }
    return render(request, 'dashboard.html', context)


def logout_paciente(request):
    logout(request)
    return redirect("login_command")
