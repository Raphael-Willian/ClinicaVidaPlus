from django.urls import path
from .views import marcar_consulta

urlpatterns = [
    path("consultas/", marcar_consulta, name = "lista_consultas")
]