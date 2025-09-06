from django.urls import path
from .views import cadastro_consulta, confirmacao
from profissionais.views import consulta_profissional

urlpatterns = [
    path("cadastro/", cadastro_consulta, name = "cadastro_consulta"),
    path("confirmacao/", confirmacao, name = "confirmacao_command"),
    path("consultas/profissionais", consulta_profissional, name = 'consulta_profissional_command')
]