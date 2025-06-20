from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Historia
from .forms import FormularioHistoria
from django.contrib.auth.mixins import LoginRequiredMixin

class CriarHistorias (CreateView):
    model = Historia
    form_class = FormularioHistoria
    template_name = 'historia/novo.html'
    success_url = reverse_lazy('listar-historias')
