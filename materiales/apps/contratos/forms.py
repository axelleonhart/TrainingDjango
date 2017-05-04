from django import forms
from apps.contratos.models import Contrato, Proveedor


class ContratoForm(forms.ModelForm):
    """
    Se declaran los campos y atributos que se mostraran en el formulario
    """
    rfc = forms.ModelChoiceField(queryset=Proveedor.objects.all(), initial=0)

    class Meta:
        model = Contrato
        exclude = ('fecha', )

        fields = [
            'id_contrato',
            'monto',
            'rfc',
            'fecha',
        ]
        labels = {
            'id_contrato': 'Contrato',
            'monto': 'Monto',
            'rfc': 'Proveedor',
            'fecha': 'Fecha',

        }
        widgets = {
            'id_contrato': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
        }
