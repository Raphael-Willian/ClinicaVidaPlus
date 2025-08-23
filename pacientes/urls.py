from django.urls import path
from .views import total_de_pacientes, logout_paciente, login_paciente, registro_paciente

urlpatterns = [
    path("total/pacientes/", total_de_pacientes, name= 'total_de_pacientes_command'),
    path("logout/", logout_paciente, name = "logout_command"),
    path("login/", login_paciente, name = "login_command"),
    path("registro/", registro_paciente, name = "registro_command")
]