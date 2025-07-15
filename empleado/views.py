from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def index(request):
    return render(request, 'empleado/index.html')

def registrar(request):
    return render(request, 'empleado/registrar.html')

def editar(request):
    return render(request, 'empleado/editar.html')