from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
        context['historia_id'] = self.historia.id
        return context

    def get_success_url(self):
        return reverse_lazy('detalhes-historia', kwargs={'pk': self.historia.id})


class DetalhesCapitulo(LoginRequiredMixin, DetailView):
    model = Capitulo
    template_name = 'capitulo/detalhes.html'

class EditarCapitulo(LoginRequiredMixin, UpdateView):
    model = Capitulo
    form_class = FormularioCapitulo
    template_name = 'capitulo/editar.html'

    def get_queryset(self):
        return Capitulo.objects.filter(historia__autor=self.request.user)
    
    def form_valid(self, form):
       # Garante que o campo historia não seja alterado
       form.instance.historia = self.object.historia
       return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ver-capitulo', kwargs={'pk': self.object.pk})

class DeletarCapitulo(LoginRequiredMixin, DeleteView):
    model = Capitulo
    template_name = 'capitulo/deletar.html'

    def get_queryset(self):
        return Capitulo.objects.filter(historia__autor=self.request.user)

    def get_success_url(self):
        return reverse_lazy('detalhes-historia', kwargs={'pk': self.object.historia.id})
