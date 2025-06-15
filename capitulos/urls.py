from django.urls import path
from capitulos.views import *

urlpatterns = [
    path('', views.index, name='index'),
]