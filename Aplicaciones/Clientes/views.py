from django.shortcuts import render,redirect
from .models import Clientes
from django.contrib import messages

def home(request):
    return render(request, "formulario.html")

def registrarUsuario(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    email = request.POST['txtEmail']
    telefono = request.POST['txtTelefono']
    documento = request.POST['txtDocumento']
    direccion = request.POST['txtDireccion']
    menorNombre = request.POST['txtNombreMenor']
    menorApellido = request.POST['txtApellidoMenor']
    parentesco = request.POST['txtParentesco']
    fecha_nacimientoMenor = request.POST['txtFeNacimiento']

    

    cliente = Clientes.objects.create(
        apellido=apellido, 
        nombre=nombre,
        email=email,
        telefono=telefono,
        documento=documento,
        direccion=direccion,
        menorNombre=menorNombre,
        menorApellido=menorApellido,
        parentesco=parentesco,
        fecha_nacimientoMenor=fecha_nacimientoMenor

        )
    

    messages.success(request, '¡Cliente registrado correctamente!')
    return redirect('/')