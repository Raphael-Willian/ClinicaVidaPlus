from django.db import models
from pacientes.models import PacientesCadastrados
from profissionais.models import Profissional
from django.core.exceptions import ValidationError
from django.utils import timezone

class Consulta(models.Model):
    pacientes = models.ForeignKey(PacientesCadastrados, on_delete=models.CASCADE, related_name="consultas")
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name="consultas")
    data = models.DateField()
    hora = models.TimeField()

    class Meta:
        unique_together = ("profissional", "data", "hora")
        # impede que o mesmo profissional tenha 2 consultas no mesmo horário

    def __str__(self):
        return f"{self.pacientes.name} - {self.profissional.name} em {self.data} às {self.hora}"

    def clean(self):
        # 1. Não pode agendar no passado
        data_hora = timezone.datetime.combine(self.data, self.hora)
        if data_hora < timezone.now():
            raise ValidationError("Não é possível agendar uma consulta no passado.")

        # 2. Verificar se já existe consulta para o mesmo profissional neste horário
        conflito = Consulta.objects.filter(
            profissional=self.profissional,
            data=self.data,
            hora=self.hora
        ).exclude(pk=self.pk)  # exclui a própria consulta caso seja edição

        if conflito.exists():
            raise ValidationError("Este horário já está ocupado para este profissional.")

    def save(self, *args, **kwargs):
        self.clean()  # chama as validações antes de salvar
        super().save(*args, **kwargs)

