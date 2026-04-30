from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    # Vista de inicio - RAMA: feature/jiliana-home
    path('', views.home, name='home'),
=======
    # Vista de inicio
    path('', views.home, name='home'),
    
    # URLs del CRUD - PARTE DE JILIANA
    path('calificaciones/', views.listar_calificaciones, name='listar_calificaciones'),
    path('calificaciones/crear/', views.crear_calificacion, name='crear_calificacion'),
    path('calificaciones/editar/<int:pk>/', views.editar_calificacion, name='editar_calificacion'),
    path('calificaciones/eliminar/<int:pk>/', views.eliminar_calificacion, name='eliminar_calificacion'),
    path('promedio-general/', views.promedio_general, name='promedio_general'),
    
    # URLs de autenticación - PARTE DE HELEN (ella las creará)
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('registro/', views.registro_view, name='registro'),
    # path('recuperar-password/', views.recuperar_password, name='recuperar_password'),
>>>>>>> feature/jiliana-configuracion
]
