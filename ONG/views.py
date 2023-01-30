from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def mascotas(request):
    return render(request, "mascotas.html")

def contacto(request):
    return render(request, "contacto.html")
