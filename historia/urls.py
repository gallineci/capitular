from django.urls import path
from historia.views import *

urlpatterns = [
    path ('',ListarHistorias.as_view(), name = 'listar-historias'),
    path ('novo/', CriarHistorias.as_view(), name='criar-historias'),
    path ('<int:pk>/', EditarHistoria.as_view(), name='editar-historia'),
    path ('deletar/<int:pk>/', DeletarHistoria.as_view(), name='deletar-historia'),
    path ('fotos/<str:arquivo>/', FotoHistoria.as_view(), name='foto-historia'),
]