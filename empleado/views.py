from django.shortcuts import render ,redirect
from .models import Empleado
from .forms import EmpleadoForm
from  django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    return render(request, 'registration/login.html')

def registration(request):
    return render(request, 'registration/regestrar.html')

def password(request):
    return render(request, 'registration/olvido_pass.html')

@login_required
def inicio(request):
    return render(request, 'paginas/inicio.html')

def index(request):
    empleado = Empleado.objects.all()
    return render(request, 'empleado/index.html' , {'empleado': empleado})


def registrar(request):
    formulario = EmpleadoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return index(request)
    return render(request, 'empleado/registrar.html', {'formulario': formulario})


def editar(request, id):
    empleado = Empleado.objects.get(id=id)
    formulario = EmpleadoForm(request.POST or None, request.FILES or None, instance=empleado)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('index')
    return render(request, 'empleado/editar.html' , {'formulario': formulario})


def eliminar(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('index')

