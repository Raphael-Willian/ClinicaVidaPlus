from django.db import models

class PacientesCadastrados(models.Model):
    nome_completo = models.CharField(max_length=120, null = False, default="sem nome")
    idade = models.IntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.nome_completo
