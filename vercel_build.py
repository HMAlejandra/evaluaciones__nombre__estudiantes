import os
import subprocess
import sys

print("=== Iniciando build de Vercel ===")

# Actualizar pip
print("Actualizando pip...")
subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

# Instalar dependencias
print("Instalando dependencias...")
subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

# Recolectar archivos estáticos
print("Recolectando archivos estáticos...")
subprocess.run([sys.executable, 'manage.py', 'collectstatic', '--noinput', '--clear'])

print("=== Build completado ===")
