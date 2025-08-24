from django.contrib.auth.models import AbstractUser
from django.db import models

class Profissional(AbstractUser):
    email = models.EmailField(unique=True)
    nome_completo = models.CharField(max_length=150)
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # remove username obrigatório

    def save(self, *args, **kwargs):
        if not self.username:
            # gera username automaticamente a partir do email
            self.username = self.email.split("@")[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_completo
