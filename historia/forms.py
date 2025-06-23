from django.forms import ModelForm
from historia.models import Historia

class FormularioHistoria(ModelForm):
    class Meta:
        model = Historia
        exclude = ['autor']
        