from django.contrib import admin

from apps.adopcion.models import Persona, Solicitud

#Registramos la aplicación de personas en el admin
admin.site.register(Persona)
admin.site.register(Solicitud)