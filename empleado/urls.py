from django.urls import path
from .views import *

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', inicio, name='inicio'),
    path('index', index , name='index'),
    path('registrar', registrar, name='registrar'),
    path('editar', editar, name='editar'),
    path('eliminar/<int:id>', eliminar, name='eliminar'),
    path('empleado/editar/<int:id>', editar, name='editar'),
 
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)