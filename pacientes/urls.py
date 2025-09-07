from django.urls import path
from profissionais.views import logout_paciente,login_profissional
from consultas.views import cadastro_consulta

urlpatterns = [
    path("logout/", logout_paciente, name = "logout_command"),
    path("login/", login_profissional, name = "login_command"),
    path("", cadastro_consulta, name = "site_command"),
]