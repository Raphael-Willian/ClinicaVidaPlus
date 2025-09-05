from django.urls import path
from .views import cadastro_consulta, confirmacao

urlpatterns = [
    path("cadastro/", cadastro_consulta, name = "cadastro_consulta"),
    path("confirmacao/", confirmacao, name = "confirmacao")
]