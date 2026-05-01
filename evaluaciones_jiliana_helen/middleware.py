"""
Middleware para asegurar que la base de datos esté inicializada en Vercel
"""
from django.core.management import call_command
from django.db import connection
import threading

# Variable global para controlar si ya se ejecutaron las migraciones
_migrations_done = False
_lock = threading.Lock()


class EnsureDatabaseMiddleware:
    """
    Middleware que asegura que las tablas de la base de datos existan
    antes de procesar cualquier request.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        global _migrations_done
        
        # Solo ejecutar migraciones una vez por instancia del servidor
        if not _migrations_done:
            with _lock:
                if not _migrations_done:
                    try:
                        # Verificar si las tablas existen
                        with connection.cursor() as cursor:
                            cursor.execute(
                                "SELECT name FROM sqlite_master WHERE type='table' AND name='auth_user'"
                            )
                            if not cursor.fetchone():
                                # Las tablas no existen, ejecutar migraciones
                                print("🔄 Ejecutando migraciones...")
                                call_command('migrate', '--noinput', verbosity=0)
                                print("✅ Migraciones completadas")
                        
                        _migrations_done = True
                    except Exception as e:
                        print(f"⚠️ Error al verificar/ejecutar migraciones: {e}")
        
        response = self.get_response(request)
        return response
