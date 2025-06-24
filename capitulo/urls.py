from django.urls import path
from capitulo.views import *

urlpatterns = [
    path('novo/<int:historia_id>/', CriarCapitulo.as_view(), name='criar-capitulo'),
    path('<int:pk>/', DetalhesCapitulo.as_view(), name='ver-capitulo'),
    path('<int:pk>/editar/', EditarCapitulo.as_view(), name='editar-capitulo'),
    path('<int:pk>/deletar/', DeletarCapitulo.as_view(), name='deletar-capitulo'),
]
