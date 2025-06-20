from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Capitulo 
from .forms import FormularioCapitulo  
from django.contrib.auth.mixins import LoginRequiredMixin

class CriarCapitulos (CreateView):
    model = Capitulo
    form_class = FormularioCapitulo
    template_name = 'capitulo/novo.html'
    success_url = reverse_lazy('listar-capitulos')
