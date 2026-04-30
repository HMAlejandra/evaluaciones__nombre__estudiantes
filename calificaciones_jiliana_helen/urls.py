from django.urls import path
from . import views

urlpatterns = [
    # Vista de inicio
    path('', views.home, name='home'),
    
    # URLs del CRUD - PARTE DE JILIANA
    path('calificaciones/', views.listar_calificaciones, name='listar_calificaciones'),
    path('calificaciones/crear/', views.crear_calificacion, name='crear_calificacion'),
    path('calificaciones/editar/<int:pk>/', views.editar_calificacion, name='editar_calificacion'),
    path('calificaciones/eliminar/<int:pk>/', views.eliminar_calificacion, name='eliminar_calificacion'),
    path('promedio-general/', views.promedio_general, name='promedio_general'),
    
    # URL de autenticación - REGISTRO (HELEN)
    path('registro/', views.registro_view, name='registro'),
    
    # URL de autenticación - RECUPERAR PASSWORD (HELEN)
    path('recuperar-password/', views.recuperar_password_view, name='recuperar_password'),
]
