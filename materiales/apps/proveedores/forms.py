from django import forms
from apps.proveedores.models import Proveedor
import re


class ProveedorForm(forms.ModelForm):
    """
    Se declaran los campos y atributos que se mostraran en el formulario
    """
    class Meta:
        model = Proveedor

        fields = [
            'nombre',
            'rfc',
            'domicilio',
            'telefono',
            'email',
        ]
        labels = {
            'nombre': 'Nombre',
            'rfc': 'RFC',
            'domicilio': 'Dirección',
            'telefono': 'Telefono',
            'email': 'Email',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rfc': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        """
        Valida que el nombre no sea menor a 5 caracteres
        """
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 5:
            raise forms.ValidationError(
                        "Debe de tener un mínimo de 5 caracteres")
        elif len(nombre) > 15:
            raise forms.ValidationError(
                        "Debe de tener un maxímo de 15 caracteres")
        return nombre

    def clean_domicilio(self):
        """
        Valida que el domicilio no sea menor a 5 caracteres
        """
        domicilio = self.cleaned_data['domicilio']
        if len(domicilio) < 5:
            raise forms.ValidationError(
                        "Debe de tener un mínimo de 5 caracteres")
        elif len(domicilio) > 15:
            raise forms.ValidationError(
                        "Debe de tener un maxímo de 15 caracteres")
        return domicilio

    def clean_telefono(self):
        """
        Valida que el telefono sea igual a 10 digitos
        """
        telefono = self.cleaned_data['telefono']
        if len(telefono) == 10:
            raise forms.ValidationError("Deben de ser 10 numeros")
        return telefono

    def clean_email(self):
        """
        Valida que el correo no esta ya registrado
        """
        email = self.cleaned_data['email']
        if Proveedor.objects.filter(email=email).exists():
            raise forms.ValidationError("El Email ya esta dado de alta")
        if not(re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',
               email.lower())):
            raise forms.ValidationError("No es un email correcto")
        return email

    def clean_rfc(self):
        """
        Valida que el rfc sea correcto
        """
        rfc = self.cleaned_data['rfc']
        if Proveedor.objects.filter(rfc=rfc).exists():
            raise forms.ValidationError("El RFC ya esta dado de alta")
        if not(re.match('^([A-Z&Ññ]{3}|[A-Z][AEIOU][A-Z]{2})\d{2}((01|03|05|07|08|10|12)(0[1-9]|[12]\d|3[01])|02(0[1-9]|[12]\d)|(04|06|09|11)(0[1-9]|[12]\d|30))([A-Z0-9]{2}[0-9A])?$',
               rfc.upper())):
            raise forms.ValidationError("No es un RFC correcto")
        return rfc
