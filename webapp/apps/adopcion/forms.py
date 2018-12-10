from django import forms

from apps.adopcion.models import Persona, Solicitud

#Creamos el formulario de personas
class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona

        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Email',
            'domicilio': 'Domicilio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
        }

#Creamos el formulario de solicitudes
class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = [
            'numero_mascota',
            'razones',
        ]
        labels = {
            'numero_mascota': 'Numero de mascotas',
            'razones': 'Razones para adoptar',
        }
        widgets = {
            'numero_mascota':forms.TextInput(attrs={'class':'form-control'}),
            'razones':forms.Textarea(attrs={'class':'form-control'}),
        }