from django.urls import path
from historia.views import *

urlpatterns = [
    path('', views.index, name='index'),
]