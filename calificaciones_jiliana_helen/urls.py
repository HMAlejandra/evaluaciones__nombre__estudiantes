from django.urls import path
from . import views

urlpatterns = [
    # Vista de inicio - RAMA: feature/jiliana-home
    path('', views.home, name='home'),
]
