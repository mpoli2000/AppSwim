from django.shortcuts import render, redirect
from AppSwim.models import *
from AppSwim.forms import *
import json

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

# Nadadores --------------------------------------------------------    

def read_nadadores(request):
    nadadores = Nadador.objects.all()
    for nadador in nadadores:
        print(type(nadador), nadador)
    return render(request, 'nadadores/read_nadadores.html', {'nadadores': nadadores})

def create_nadadores(request):
    if request.method == 'POST':
        nadador = Nadador(nombre = request.POST['nombre'],
                          apellido = request.POST['apellido'],
                          email = request.POST['email'],
                          edad = request.POST['edad'])
        nadador.save()
        return redirect('/AppSwim/read_nadadores')
        # nadadores = Nadador.objects.all()
        # return render(request, 'nadadores/read_nadadores.html', {'nadadores': nadadores})
    return render(request, 'nadadores/create_nadadores.html')

def delete_nadadores(request, id_nadador):
    nadador = Nadador.objects.get(id = id_nadador)
    nadador.delete()

    return redirect('/AppSwim/read_nadadores')
    # nadadores = Nadador.objects.all()
    # return render(request, 'nadadores/read_nadadores.html', {'nadadores': nadadores})
    
def update_nadadores(request, id_nadador):
    nadador = Nadador.objects.get(id = id_nadador)
    if request.method == 'POST':
        formulario = Form_Nadador(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nadador.nombre = info['nombre']
            nadador.apellido = info['apellido']
            nadador.email = info['email']
            nadador.edad = info['edad']
            nadador.save()

            return redirect('/AppSwim/read_nadadores')
            # nadadores = Nadador.objects.all()
            # return render(request, 'nadadores/read_nadadores.html', {'nadadores': nadadores})
    else:
        formulario = Form_Nadador(initial={'nombre': nadador.nombre,
                                           'apellido': nadador.apellido,
                                           'email': nadador.email,
                                           'edad': nadador.edad})
        return render(request, 'nadadores/update_nadadores.html', {'formulario': formulario})


# Profesores -----------------------------------------------------------------------------
def read_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores/read_profesores.html', {'profesores': profesores})

def create_profesores(request):
    if request.method == 'POST':
        profesor = Profesor(nombre = request.POST['nombre'],
                          apellido = request.POST['apellido'],
                          email = request.POST['email'])
        profesor.save()

        return redirect('/AppSwim/read_profesores')
        # profesores = Profesor.objects.all()
        # return render(request, 'profesores/read_profesores.html', {'profesores': profesores})
    return render(request, 'profesores/create_profesores.html')

def delete_profesores(request, id_profesor):
    profesor = Profesor.objects.get(id = id_profesor)
    profesor.delete()

    return redirect('/AppSwim/read_profesores')
    # profesores = Profesor.objects.all()
    # return render(request, 'profesores/read_profesores.html', {'profesores': profesores})
    
def update_profesores(request, id_profesor):
    profesor = Profesor.objects.get(id = id_profesor)
    if request.method == 'POST':
        formulario = Form_Profesor(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            profesor.nombre = info['nombre']
            profesor.apellido = info['apellido']
            profesor.email = info['email']
            profesor.save()

            return redirect('/AppSwim/read_profesores')
            # profesores = Profesor.objects.all()
            # return render(request, 'profesores/read_profesores.html', {'profesores': profesores})
    else:
        formulario = Form_Profesor(initial={'nombre': profesor.nombre,
                                           'apellido': profesor.apellido,
                                           'email': profesor.email})
        return render(request, 'profesores/update_profesores.html', {'formulario': formulario})


# Estilos --------------------------------------------------------------------
def read_estilos(request):
    estilos = Estilo.objects.all()
    return render(request, 'estilos/read_estilos.html', {'estilos': estilos})

def create_estilos(request):
    if request.method == 'POST':
        estilo = Estilo(nombre = request.POST['nombre'],
                        descripcion = request.POST['descripcion'])
        estilo.save()
        
        return redirect('/AppSwim/read_estilos')
        # estilos = Estilo.objects.all()
        # return render(request, 'estilos/read_estilos.html', {'estilos': estilos})
    return render(request, 'estilos/create_estilos.html')

def delete_estilos(request, id_estilo):
    estilo = Estilo.objects.get(id = id_estilo)
    estilo.delete()
    
    return redirect('/AppSwim/read_estilos')
    # estilos = Estilo.objects.all()
    # return render(request, 'estilos/read_estilos.html', {'estilos': estilos})
    
def update_estilos(request, id_estilo):
    estilo = Estilo.objects.get(id = id_estilo)
    if request.method == 'POST':
        formulario = Form_Estilo(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            estilo.nombre = info['nombre']
            estilo.descripcion = info['descripcion']
            estilo.save()

            return redirect('/AppSwim/read_estilos')
            # estilos = Estilo.objects.all()
            # return render(request, 'estilos/read_estilos.html', {'estilos': estilos})
    else:
        formulario = Form_Estilo(initial={'nombre': estilo.nombre,
                                           'descripcion': estilo.descripcion})
        return render(request, 'estilos/update_estilos.html', {'formulario': formulario})


# Slots ---------------------------------------------------------------------
def read_slots(request):
    slots = Slot.objects.all()
    return render(request, 'slots/read_slots.html', {'slots': slots})

def create_slots(request):
    if request.method == 'POST':
        slot = Slot(fecha = request.POST['fecha'],
                    horario = request.POST['horario'],
                    duracion = request.POST['duracion'])
        slot.save()
        slots = Slot.objects.all()
        return render(request, 'slots/read_slots.html', {'slots': slots})
    return render(request, 'slots/create_slots.html')

def delete_slots(request, id_slot):
    slot = Slot.objects.get(id = id_slot)
    slot.delete()
    
    slots = Slot.objects.all()
    return render(request, 'slots/read_slots.html', {'slots': slots})
    
def update_slots(request, id_slot):
    slot = Slot.objects.get(id = id_slot)
    if request.method == 'POST':
        formulario = Form_Slot(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            slot.nombre = info['fecha']
            slot.apellido = info['horario']
            slot.email = info['duracion']
            slot.save()

        slots = Slot.objects.all()
        return render(request, 'slots/read_slots.html', {'slots': slots})
    else:
        formulario = Form_Slot(initial={'fecha': slot.fecha,
                                        'horario': slot.horario,
                                        'duracion': slot.duracion})
        return render(request, 'slots/update_slots.html', {'formulario': formulario})