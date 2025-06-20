from django.urls import path
from capitulo.views import *

urlpatterns = [
    path('novo/', CriarCapitulo.as_view(), name='cadastrar-capitulo'),
]