from django.urls import path
from historia.views import *

urlpatterns = [
    path ('novo/', CriarHistorias.as_view(), name='criar-historias'),
]