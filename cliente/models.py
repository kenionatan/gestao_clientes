from django.db import models
from django.conf import settings

class Cliente(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    nome_cliente = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_cliente
