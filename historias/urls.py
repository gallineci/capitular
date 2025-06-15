from django.urls import path
from historias.views import *

urlpatterns = [
    path('', views.index, name='index'),
]