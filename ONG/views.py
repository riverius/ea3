from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contacto
from .forms import ContactoForm, NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


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

def perritos(request):
    return render(request, "perritos.html")

def gatitos(request):
    return render (request, 'gatitos.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Usuario registrado." )
			return redirect(to="home")
		messages.error(request, "Información inválida.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Has iniciado sesión como {username}.")
				return redirect(to="home")
			else:
				messages.error(request,"Usuario o contraseña inválidos.")
		else:
			messages.error(request,"Usuario o contraseña inválidos.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def salir(request):
    logout(request)
    return redirect('/')

def hora(request):
    return render (request, 'hora.html')