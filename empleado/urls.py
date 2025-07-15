from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('index', index , name='index'),
    path('registrar', registrar, name='registrar'),
    path('editar', editar, name='editar'),
   
]