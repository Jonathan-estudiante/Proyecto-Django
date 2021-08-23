from django import forms
from .models import *

class EstudianteForm(forms.ModelForm):
    class Meta: 
        model = Estudiante
        fields = [
            'nombres',
            'apellidos',
            'carrera',
            'edad',
            'telefono'
        ]