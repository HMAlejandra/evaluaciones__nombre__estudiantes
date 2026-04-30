from django.contrib import admin
from .models import Calificacion

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Calificacion
    """
    list_display = ['nombre_estudiante', 'identificacion', 'asignatura', 'nota1', 'nota2', 'nota3', 'promedio']
    list_filter = ['asignatura']
    search_fields = ['nombre_estudiante', 'identificacion', 'asignatura']
    readonly_fields = ['promedio']
    
    fieldsets = (
        ('Información del Estudiante', {
            'fields': ('nombre_estudiante', 'identificacion', 'asignatura')
        }),
        ('Calificaciones', {
            'fields': ('nota1', 'nota2', 'nota3', 'promedio')
        }),
    )
