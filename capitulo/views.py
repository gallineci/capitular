from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Capitulo
from .forms import FormularioCapitulo
from historia.models import Historia
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

class CriarCapitulo(LoginRequiredMixin, CreateView):
    model = Capitulo
    form_class = FormularioCapitulo
    template_name = 'capitulo/novo.html'

    def dispatch(self, request, *args, **kwargs):
        self.historia = get_object_or_404(Historia, id=kwargs['historia_id'])
        if self.historia.autor != request.user:
            return HttpResponseForbidden("Você não tem permissão para adicionar capítulos a essa história.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.historia = self.historia
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historia_id'] = self.historia.id  # usado em novo.html
        return context

    def get_success_url(self):
        return reverse_lazy('ver-historia', kwargs={'pk': self.historia.id})


class DetalhesCapitulo(LoginRequiredMixin, DetailView):
    model = Capitulo
    template_name = 'capitulo/detalhes.html'
