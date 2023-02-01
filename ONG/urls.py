from django.urls import path
from .views import home, salir, mascotas, contacto, form_del_contacto, form_mod_contacto, datos, form_contacto_ext, perritos, gatitos, register_request, login_request


urlpatterns = [
    path('', home,name='home'),
    path('mascotas/', mascotas,name='mascota'),
    path('contacto/', contacto,name='contacto'),
    path('datos/', datos,name="datos"),
    path('form-contacto-ext/>', form_contacto_ext, name="form_contacto_ext"),
    path('form-mod-contacto/<tel>', form_mod_contacto, name="form_mod_contacto"),
    path('form-del-contacto/<tel>', form_del_contacto, name="form_del_contacto"),
    path('perritos/', perritos, name='perritos'),
    path('gatitos/', gatitos, name='gatitos'),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("salir", salir, name= "salir"),
]