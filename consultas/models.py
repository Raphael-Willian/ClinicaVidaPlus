from email.policy import default

from django.db import models
from pacientes.models import PacientesCadastrados
from profissionais.models import Profissional

class Consulta(models.Model):

    PAGAMENTO_CHOICE = [
        ('PAGO', 'PAGO'),
        ('PENDENTE', 'PENDENTE'),
        ('CANCELADO', 'CANCELADO'),
        ('ATRASADO', 'ATRASADO')
    ]

    pacientes = models.ForeignKey(PacientesCadastrados, on_delete=models.CASCADE, related_name="consultas")
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name="consultas")
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_do_fim = models.TimeField()
    observacoes = models.TextField()
    valor_da_consulta = models.FloatField(default=70)
    data_de_registro = models.DateTimeField(auto_now_add=True)
    status_do_pagamento = models.CharField(max_length = 10, default = 'PENDENTE', choices = PAGAMENTO_CHOICE)

    class Meta:
        unique_together = ("profissional", "data", "hora_inicio")


    def __str__(self):
        return f"{self.pacientes.nome_completo} - {self.profissional.nome_completo} em {self.data} às {self.hora_inicio}"
