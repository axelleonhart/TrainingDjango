from django import forms
from apps.clientes.models import Cliente
from apps.clientes.choices import SEXO_CHOICES
import re


class ClienteForm(forms.ModelForm):
    """
    Se declaran los campos y atributos que se mostraran en el formulario
    """
    sexo = forms.ChoiceField(choices=SEXO_CHOICES, required=True)

    class Meta:
        model = Cliente

        fields = [
            'nombre',
            'sexo',
            'direccion',
            'email',
            'fecha_nac',
        ]
        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'direccion': 'Dirección',
            'email': 'Email',
            'fecha_nac': 'Fecha de Nacimiento',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'fecha_nac': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        """
        Valida que el nombre no sea menor a 3 caracteres
        """
        nombre_lim = self.cleaned_data
        nombre = nombre_lim.get('nombre')

        if len(nombre) < 5:
            raise forms.ValidationError(
                   "Debe de tener un mínimo de 5 caracteres")
        elif len(nombre) > 15:
            raise forms.ValidationError(
                   "Debe de tener un maxímo de 15 caracteres")
        return nombre

    def clean_email(self):
        """
        Valida que el correo no esta ya registrado
        """
        email = self.cleaned_data['email']
        if Cliente.objects.filter(email=email).exists():
            raise forms.ValidationError("El Email ya esta dado de alta")
        if not(re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',
               email.lower())):
            raise forms.ValidationError("No es un email correcto")
        return email

    def clean_direccion(self):
        """
        Valida que la dirección no sea menor a 5 caracteres
        """
        direccion = self.cleaned_data['direccion']
        if len(direccion) < 5:
            raise forms.ValidationError(
                  "Debe de tener un mínimo de 5 caracteres")
        elif len(direccion) > 15:
            raise forms.ValidationError(
                  "Debe de tener un maxímo de 5 caracteres")
        return direccion
