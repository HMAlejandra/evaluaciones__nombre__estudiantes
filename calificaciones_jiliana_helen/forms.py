from django import forms
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    """
    Formulario para crear y editar calificaciones.
    El campo promedio se excluye porque se calcula automáticamente.
    """
    class Meta:
        model = Calificacion
        fields = ['nombre_estudiante', 'identificacion', 'asignatura', 'nota1', 'nota2', 'nota3']
        widgets = {
            'nombre_estudiante': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre completo del estudiante'
            }),
            'identificacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la identificación'
            }),
            'asignatura': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre de la asignatura'
            }),
            'nota1': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0',
                'max': '100'
            }),
            'nota2': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0',
                'max': '100'
            }),
            'nota3': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0',
                'max': '100'
            }),
        }
