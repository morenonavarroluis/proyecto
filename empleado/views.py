from pyexpat.errors import messages
from django.shortcuts import render ,redirect
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse


# Create your views here.

def login(request):
    # usar get para mostrar el formulario de inicio de sesión
    if request.method == 'GET':
        return render(request, 'registration/login.html', {'form': AuthenticationForm()})

    # usar post para autenticar al usuario
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        return redirect('inicio')  # redirecciona a la página de inicio
    else:
        #retorna un error si las credenciales son incorrectas
        return render(request, 'registration/login.html', {
            'form': AuthenticationForm(),
            'error': 'Usuario o contraseña incorrectos'
        })


def registration(request):
    if request.method == 'GET':

        return render(request, 'registration/regestrar.html', {'form': UserCreationForm()})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try: 
               user = User.objects.create_user(
               username=request.POST['username'],
               email=request.POST['email'],
               password=request.POST['password1'] )
               user.save()
               return render(request, 'registration/regestrar.html', {'form': UserCreationForm(), 'success': 'Usuario creado exitosamente'})
            except:
                return render(request, 'registration/regestrar.html', {'form': UserCreationForm, 'error': 'Error al crear el usuario. El nombre de usuario ya existe.'})
        return render(request, 'registration/regestrar.html', {'form': UserCreationForm, 'error': 'Las contraseñas no coinciden.'})
     

def password(request):
    return render(request, 'registration/olvido_pass.html')

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



