from django import forms
from apps.clientes.models import Cliente 
from apps.clientes.choices import SEXO_CHOICES

class ClienteForm(forms.ModelForm):
	sexo = forms.ChoiceField(choices = SEXO_CHOICES, required=True)
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
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			'fecha_nac': forms.TextInput(attrs={'class':'form-control'}),
		}
