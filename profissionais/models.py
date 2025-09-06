from django.contrib.auth.models import AbstractUser
from django.db import models

class Profissional(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    nome_completo = models.CharField(max_length=150)
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, default="")
    genero = models.CharField(max_length=20)
    endereco = models.TextField(max_length=100)
    cep = models.CharField(max_length=10)
    registro_profissional = models.CharField(max_length=25)
    status = models.CharField(max_length=10)
    comissao = models.FloatField(null=True, blank=True)


    REQUIRED_FIELDS = []  # remove username obrigatório

    def save(self, *args, **kwargs):
        if not self.username:
            # gera username automaticamente a partir do email
            self.username = self.email.split("@")[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_completo
