from django.shortcuts import render, redirect
from .models import Contacto
from .forms import ContactoForm


def home(request):
    return render(request, "home.html")


def mascotas(request):
    return render(request, "mascotas.html")


def contacto(request):
    return render(request, "contacto.html")


def datos(request):
    contactos = Contacto.objects.all()
    datos = {'Contactos':contactos}
    return render(request, 'datos.html', datos)


def form_contacto_ext(request):
    datos = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"
    return render(request, 'form_contacto_ext.html', datos)


def form_mod_contacto(request, tel):
    contacto = Contacto.objects.get(telefono=tel)
    datos = {
        'form': ContactoForm(instance=contacto)
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST, instance=contacto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"
    return render(request, 'form_mod_contacto.html', datos)


def form_del_contacto(request, tel):
    contacto = Contacto.objects.get(telefono=tel)
    contacto.delete()
    return redirect(to="datos")
