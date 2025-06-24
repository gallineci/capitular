from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic import View
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
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
    
class EditarHistoria (LoginRequiredMixin, UpdateView):
    model = Historia
    form_class = FormularioHistoria
    template_name = 'historia/editar.html'
    success_url = reverse_lazy('listar-historias')

class DeletarHistoria (LoginRequiredMixin, DeleteView):
    model = Historia
    template_name = 'historia/deletar.html'
    success_url = reverse_lazy('listar-historias')

class DetalhesHistoria(LoginRequiredMixin, DetailView):
    model = Historia
    template_name = 'historia/detalhes.html'


class FotoHistoria (View):
    def get (self, request, arquivo):
        try:
            historia = Historia.objects.get (foto='historia/fotos/{}'.format(arquivo))
            return FileResponse (historia.foto)
        except ObjectDoesNotExist:
            raise Http404 ("Foto não encontrada ou acesso não autorizado")
        except Exception as exception:
            raise exception 