from django.conf import settings
from django.db import models

class PacientesCadastrados(models.Model):
    profissional = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=120)
    idade = models.IntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=16, blank=True, null=True)
    rg = models.CharField(max_length=10, unique=True, blank=False, default=None)
    cpf = models.CharField(max_length=11, unique=True, blank=False, default=None)

    def __str__(self):
        return self.nome_completo
