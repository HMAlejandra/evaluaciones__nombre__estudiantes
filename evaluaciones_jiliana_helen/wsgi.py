"""
WSGI config for evaluaciones_jiliana_helen project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaluaciones_jiliana_helen.settings')

# Ejecutar migraciones automáticamente en Vercel
from django.core.management import execute_from_command_line
try:
    execute_from_command_line(['manage.py', 'migrate', '--noinput'])
    print("✅ Migraciones ejecutadas correctamente")
except Exception as e:
    print(f"⚠️ Error al ejecutar migraciones: {e}")

application = get_wsgi_application()

# Vercel handler
app = application
