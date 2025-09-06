from django.db import models
from pacientes.models import PacientesCadastrados
from profissionais.models import Profissional

class Consulta(models.Model):
    pacientes = models.ForeignKey(PacientesCadastrados, on_delete=models.CASCADE, related_name="consultas")
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name="consultas")
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_do_fim = models.TimeField()
    observacoes = models.TextField()
    valor_da_consulta = models.FloatField(default=70)
    data_de_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("profissional", "data", "hora_inicio")
        # impede que o mesmo profissional tenha 2 consultas no mesmo horário

    def __str__(self):
        return f"{self.pacientes.nome_completo} - {self.profissional.nome_completo} em {self.data} às {self.hora_inicio}"
