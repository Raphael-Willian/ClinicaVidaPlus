from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pacientes.models import PacientesCadastrados
from django.db.models import Avg
from pacientes.forms import PacienteForm

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


def login_profissional(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect("total_de_pacientes_command")
        else:
            return render(request, "login.html", {"error": "Email ou senha inválidos"})
    return render(request, "login.html")


def logout_paciente(request):
    logout(request)
    return redirect("login_command")
