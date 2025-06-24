from django.urls import path
from capitulo.views import *

urlpatterns = [
    path('novo/<int:historia_id>/', CriarCapitulo.as_view(), name='criar-capitulo'),
    path('<int:pk>/', DetalhesCapitulo.as_view(), name='ver-capitulo'),
]
