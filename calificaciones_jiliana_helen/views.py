from django.shortcuts import render

# ============================================
# VISTA HOME - PARTE DE JILIANA
# ============================================

def home(request):
    """Vista de inicio/home - Accesible para todos"""
    return render(request, 'home.html')
