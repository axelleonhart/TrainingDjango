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
