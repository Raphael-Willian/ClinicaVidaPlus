from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from .models import PacientesCadastrados
from django.db.models import Avg
from .forms import RegistroForm

@login_required(login_url="login_command")
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
    return HttpResponseNotAllowed(['GET'])

def registro_paciente(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            PacientesCadastrados.objects.create(
                user = user,
                nome_completo = form.cleaned_data["nome_completo"],
                idade = form.cleaned_data["idade"],
                telefone = form.cleaned_data["telefone"]
            )
        return redirect("login_command")

    else:
        form = RegistroForm()
    return render(request, "register.html", {"form":form})

def login_paciente(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("total_de_pacientes_command")
        else:
            return render(request, "login.html", {"error": "Usuário ou senha inválidos"})

    return render(request, "login.html")

def logout_paciente(request):
    logout(request)
    return redirect("login_command")