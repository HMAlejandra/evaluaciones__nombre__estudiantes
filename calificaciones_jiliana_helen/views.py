from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg
from .models import Calificacion
from .forms import CalificacionForm

# ============================================
# VISTAS PÚBLICAS
# ============================================

def home(request):
    """Vista de inicio/home - Accesible para todos"""
    return render(request, 'home.html')


# ============================================
# VISTAS DEL CRUD - PARTE DE JILIANA
# ============================================

@login_required
def listar_calificaciones(request):
    """
    Vista para listar todas las calificaciones registradas.
    También muestra el promedio general de todos los estudiantes.
    """
    calificaciones = Calificacion.objects.all()
    
    # Calcular el promedio general usando la función agregada Avg
    promedio_general = Calificacion.objects.all().aggregate(Avg('promedio'))['promedio__avg']
    
    # Si no hay calificaciones, el promedio será None
    if promedio_general is None:
        promedio_general = 0
    else:
        promedio_general = round(promedio_general, 2)
    
    context = {
        'calificaciones': calificaciones,
        'promedio_general': promedio_general,
        'total_registros': calificaciones.count()
    }
    
    return render(request, 'calificaciones/listar.html', context)


@login_required
def crear_calificacion(request):
    """
    Vista para crear una nueva calificación.
    El promedio se calcula automáticamente al guardar.
    """
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            calificacion = form.save()
            messages.success(request, f'¡Calificación registrada exitosamente! Promedio: {calificacion.promedio}')
            return redirect('listar_calificaciones')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CalificacionForm()
    
    return render(request, 'calificaciones/crear.html', {'form': form})


@login_required
def editar_calificacion(request, pk):
    """
    Vista para editar una calificación existente.
    El promedio se recalcula automáticamente al guardar.
    """
    calificacion = get_object_or_404(Calificacion, pk=pk)
    
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            calificacion = form.save()
            messages.success(request, f'¡Calificación actualizada exitosamente! Nuevo promedio: {calificacion.promedio}')
            return redirect('listar_calificaciones')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CalificacionForm(instance=calificacion)
    
    return render(request, 'calificaciones/editar.html', {'form': form, 'calificacion': calificacion})


@login_required
def eliminar_calificacion(request, pk):
    """
    Vista para eliminar una calificación.
    Muestra una página de confirmación antes de eliminar.
    """
    calificacion = get_object_or_404(Calificacion, pk=pk)
    
    if request.method == 'POST':
        nombre = calificacion.nombre_estudiante
        asignatura = calificacion.asignatura
        calificacion.delete()
        messages.success(request, f'Calificación de {nombre} en {asignatura} eliminada exitosamente.')
        return redirect('listar_calificaciones')
    
    return render(request, 'calificaciones/eliminar.html', {'calificacion': calificacion})


@login_required
def promedio_general(request):
    """
    Vista dedicada para mostrar el promedio general de todos los estudiantes.
    Utiliza la función agregada Avg de Django.
    """
    # Calcular el promedio general
    resultado = Calificacion.objects.all().aggregate(Avg('promedio'))
    promedio = resultado['promedio__avg']
    
    if promedio is None:
        promedio = 0
    else:
        promedio = round(promedio, 2)
    
    # Obtener estadísticas adicionales
    total_estudiantes = Calificacion.objects.count()
    
    context = {
        'promedio_general': promedio,
        'total_estudiantes': total_estudiantes,
    }
    
    return render(request, 'calificaciones/promedio_general.html', context)


# ============================================
# VISTA LOGIN - PARTE DE HELEN
# ============================================

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    """Vista personalizada para el inicio de sesión."""
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')
