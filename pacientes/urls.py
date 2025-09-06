from django.urls import path
from profissionais.views import total_de_pacientes, logout_paciente,login_profissional
from consultas.views import cadastro_consulta

urlpatterns = [
    path("pacientes/", total_de_pacientes, name= 'total_de_pacientes_command'),
    path("logout/", logout_paciente, name = "logout_command"),
    path("login/", login_profissional, name = "login_command"),
    path("", cadastro_consulta, name = "site_command"),
]