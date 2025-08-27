from django.shortcuts import render, redirect
from .models import Consulta
from .forms import ConsultaForm
from django.contrib import messages

def marcar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Consulta marcada com sucesso!")
            return redirect("lista_consultas")

        else:
            messages.error(request,"Erro ao marcar consulta. Verifique os campos")

    else:
        form = ConsultaForm()

    return render(request, "consultas.html", {"form": form})



