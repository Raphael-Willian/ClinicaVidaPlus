from django.db import models
from django.contrib.auth.models import User

class PacientesCadastrados(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome_completo = models.CharField(max_length=120, null = False, default="sem nome")
    idade = models.IntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.nome_completo
