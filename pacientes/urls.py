from django.urls import path
from .views import total_de_pacientes

urlpatterns = [
    path("total/pacientes/", total_de_pacientes, name= 'total_de_pacientes_command'),
]