from django.urls import path
from historia.views import *

urlpatterns = [
    path ('',ListarHistorias.as_view(), name = 'listar-historias'),
    path ('novo/', CriarHistorias.as_view(), name='criar-historias'),
]