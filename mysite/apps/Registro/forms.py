from django import forms
from .models import Bicicleta, Portico


class porticoForm(forms.ModelForm):
    class Meta:
        model = Portico
        fields = ['id_portico', 'ubicacion']

        labels = {
            'id_portico': 'ID',
            'ubicacion': 'Ubicacion',

        }
        widgets = {
            'id_portico': forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
