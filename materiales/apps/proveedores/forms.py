from django import forms
from apps.proveedores.models import Proveedor


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
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        """
        Valida que el nombre no sea menor a 5 caracteres 
        """
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 5:
            raise forms.ValidationError("Debe de tener un minimo de 5 caracteres")
        return nombre

    def clean_domicilio(self):
        """
        Valida que el domicilio no sea menor a 5 caracteres 
        """
        domicilio = self.cleaned_data['domicilio']
        if len(domicilio) < 5:
            raise forms.ValidationError("Debe de tener un minimo de 5 caracteres")
        return domicilio

    def clean_telefono(self):
        """
        Valida que el telefono sea igual a 10 caracteres 
        """
        telefono = self.cleaned_data['telefono']
        if not(isinstance(telefono, int)) and len(telefono) < 10:
            raise forms.ValidationError("Debe de ser de 10 numeros")
        return telefono