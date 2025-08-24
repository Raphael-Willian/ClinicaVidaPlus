from django.urls import path
from profissionais.views import total_de_pacientes, logout_paciente,login_profissional

urlpatterns = [
    path("total/pacientes/", total_de_pacientes, name= 'total_de_pacientes_command'),
    path("logout/", logout_paciente, name = "logout_command"),
    path("login/", login_profissional, name = "login_command"),
]