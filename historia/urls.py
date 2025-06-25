from django.urls import path
from historia.views import *

urlpatterns = [
    path ('',ListarHistorias.as_view(), name = 'listar-historias'),
    path('api/', ListarHistoriasAPI.as_view(), name='api-historias'),
    path ('novo/', CriarHistorias.as_view(), name='criar-historias'),
    path ('<int:pk>/', EditarHistoria.as_view(), name='editar-historia'),
    path('api/<int:pk>/', DeletarHistoriaAPI.as_view(), name='api-deletar-historia'),
    path ('deletar/<int:pk>/', DeletarHistoria.as_view(), name='deletar-historia'),
    path('detalhes/<int:pk>/', DetalhesHistoria.as_view(), name='detalhes-historia'),
    path ('fotos/<str:arquivo>/', FotoHistoria.as_view(), name='foto-historia'),
]