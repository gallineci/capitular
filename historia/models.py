from django.db import models
from django.contrib.auth.models import User
from .consts import OPCOES_GENEROS, OPCOES_ESTILOS, OPCOES_STATUS

class Historia(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    genero = models.IntegerField(choices=OPCOES_GENEROS)
    estilo = models.IntegerField(choices=OPCOES_ESTILOS, blank=True, null=True)
    status = models.IntegerField(choices=OPCOES_STATUS, default=1)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.get_genero_display()})"
