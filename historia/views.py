from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Historia
from .forms import FormularioHistoria

class ListarHistorias(LoginRequiredMixin, ListView):
    model = Historia
    context_object_name = 'historias'
    template_name = 'historia/listar.html'

class CriarHistorias(LoginRequiredMixin, CreateView):
    model = Historia
    form_class = FormularioHistoria
    template_name = 'historia/novo.html'
    success_url = reverse_lazy('listar-historias')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
