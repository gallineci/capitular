from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Historia
from .forms import FormularioHistoria
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from historia.serializer import HistoriaSerializer

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

class EditarHistoria(LoginRequiredMixin, UpdateView):
    model = Historia
    form_class = FormularioHistoria
    template_name = 'historia/editar.html'
    success_url = reverse_lazy('listar-historias')

class DeletarHistoria(LoginRequiredMixin, DeleteView):
    model = Historia
    template_name = 'historia/deletar.html'
    success_url = reverse_lazy('listar-historias')

class DetalhesHistoria(LoginRequiredMixin, DetailView):
    model = Historia
    template_name = 'historia/detalhes.html'

class FotoHistoria(View):
    def get(self, request, arquivo):
        try:
            historia = Historia.objects.get(foto=f'historia/fotos/{arquivo}')
            return FileResponse(historia.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não autorizado")
        except Exception as exception:
            raise exception

# ===== api views =====

class ListarHistoriasAPI(ListAPIView):
    serializer_class = HistoriaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Historia.objects.all()

class DeletarHistoriaAPI(DestroyAPIView):
    serializer_class = HistoriaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Historia.objects.all()
