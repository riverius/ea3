from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('mascotas/', views.mascotas,name='mascota'),
    path('contacto/', views.contacto,name='contacto'),
    path('perritos/', views.perritos, name='perritos'),
    path('gatitos/', views.gatitos, name='gatitos'),
]