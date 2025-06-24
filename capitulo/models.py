from django.db import models
from historia.models import Historia

class Capitulo(models.Model):
    titulo = models.CharField(max_length=200)
    notas_autor = models.TextField(blank=True)
    arquivo_capitulo = models.FileField(upload_to='capitulos/', blank=True, null=True)
    historia = models.ForeignKey(Historia, on_delete=models.CASCADE, related_name='capitulos')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.historia.titulo})"
