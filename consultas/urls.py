from django.urls import path
from .views import cadastro_consulta, confirmacao
from profissionais.views import consulta_profissional
from profissionais.views import total_de_pacientes
from profissionais.views import configuracoes, dashboard

urlpatterns = [
    path("cadastro/", cadastro_consulta, name = "cadastro_consulta"),
    path("confirmacao/", confirmacao, name = "confirmacao_command"),
    path("consultas/profissionais", consulta_profissional, name = 'consulta_profissional_command'),
    path("pacientes/", total_de_pacientes, name= 'total_de_pacientes_command'),
    path("configuracoes/", configuracoes, name="configuracoes_command"),
    path('dashboard/', dashboard, name='dashboard_command'),
]