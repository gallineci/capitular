from django.forms import ModelForm
from .models import Capitulo

class FormularioCapitulo(ModelForm):
    class Meta:
        model = Capitulo
        fields = ['titulo', 'descricao', 'conteudo'] 
