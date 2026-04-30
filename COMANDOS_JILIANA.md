# 🚀 Comandos Paso a Paso para Jiliana

## 📝 PARTE 1: Probar el Proyecto Localmente

### 1. Crear un superusuario para acceder al admin

```bash
python manage.py createsuperuser
```

Te pedirá:
- **Username**: Elige un nombre de usuario (ejemplo: `admin` o `jiliana`)
- **Email**: Puedes dejarlo en blanco o poner tu email
- **Password**: Elige una contraseña (mínimo 8 caracteres)
- **Password (again)**: Repite la contraseña

### 2. Ejecutar el servidor

```bash
python manage.py runserver
```

### 3. Probar en el navegador

Abre tu navegador y visita:

- **Página de inicio**: http://127.0.0.1:8000/
- **Admin de Django**: http://127.0.0.1:8000/admin/
- **Lista de calificaciones**: http://127.0.0.1:8000/calificaciones/
- **Crear calificación**: http://127.0.0.1:8000/calificaciones/crear/
- **Promedio general**: http://127.0.0.1:8000/promedio-general/

### 4. Probar el CRUD completo

1. **Inicia sesión** con el superusuario que creaste
2. **Crea** algunas calificaciones de prueba
3. **Edita** una calificación
4. **Elimina** una calificación
5. **Verifica** que el promedio se calcula automáticamente
6. **Revisa** el promedio general

## 📝 PARTE 2: Subir a GitHub

### 1. Crear un repositorio en GitHub

1. Ve a https://github.com
2. Haz clic en el botón **"New"** (verde)
3. Nombre del repositorio: `sistema-calificaciones-django`
4. Descripción: `Sistema de gestión de calificaciones con Django - Laboratorio Final`
5. Selecciona **"Public"** o **"Private"** según prefieras
6. **NO** marques "Add a README file" (ya lo tenemos)
7. **NO** marques "Add .gitignore" (ya lo tenemos)
8. Haz clic en **"Create repository"**

### 2. Inicializar Git y hacer el primer commit

```bash
# 1. Inicializar Git (si no está inicializado)
git init

# 2. Agregar todos los archivos
git add .

# 3. Ver qué archivos se van a subir
git status

# 4. Hacer el primer commit
git commit -m "feat: implementación completa del CRUD de calificaciones con diseño moderno"

# 5. Renombrar la rama a main (si es necesario)
git branch -M main
```

### 3. Conectar con GitHub y subir

```bash
# Reemplaza <TU_USUARIO> con tu usuario de GitHub
git remote add origin https://github.com/<TU_USUARIO>/sistema-calificaciones-django.git

# Subir a GitHub
git push -u origin main
```

### 4. Crear la rama develop

```bash
# Crear rama develop
git checkout -b develop

# Subir develop a GitHub
git push -u origin develop
```

### 5. Crear tu rama de feature

```bash
# Crear tu rama de trabajo
git checkout -b feature/jiliana-crud

# Subir tu rama
git push -u origin feature/jiliana-crud
```

### 6. Hacer merge a develop

```bash
# Volver a develop
git checkout develop

# Hacer merge de tu feature
git merge feature/jiliana-crud

# Subir los cambios
git push origin develop
```

## 📝 PARTE 3: Preparar para que Helen trabaje

### 1. Compartir el repositorio con Helen

1. Ve a tu repositorio en GitHub
2. Haz clic en **"Settings"**
3. En el menú izquierdo, haz clic en **"Collaborators"**
4. Haz clic en **"Add people"**
5. Busca a Helen por su usuario de GitHub
6. Envíale la invitación

### 2. Enviarle las instrucciones a Helen

Comparte con Helen:
- La URL del repositorio
- El archivo `INSTRUCCIONES_HELEN.md`
- Dile que debe trabajar en la rama `feature/helen-auth`

## 📝 PARTE 4: Cuando Helen termine su parte

### 1. Revisar el Pull Request de Helen

1. Ve a tu repositorio en GitHub
2. Haz clic en **"Pull requests"**
3. Verás el PR de Helen: `feature/helen-auth` → `develop`
4. Revisa los cambios
5. Si todo está bien, haz clic en **"Merge pull request"**
6. Confirma el merge

### 2. Actualizar tu repositorio local

```bash
# Cambiar a develop
git checkout develop

# Traer los cambios de GitHub
git pull origin develop
```

### 3. Probar todo junto

```bash
# Ejecutar el servidor
python manage.py runserver

# Probar:
# - Login
# - Registro
# - CRUD de calificaciones
# - Logout
```

## 📝 PARTE 5: Preparar para Vercel (Despliegue)

### 1. Instalar dependencias adicionales

```bash
pip install gunicorn whitenoise
pip freeze > requirements.txt
```

### 2. Crear archivo vercel.json

Ya está creado, pero verifica que exista en la raíz del proyecto.

### 3. Modificar settings.py para producción

Abre `evaluaciones_jiliana_helen/settings.py` y agrega al final:

```python
# Configuración para producción
import os

if os.environ.get('VERCEL_ENV'):
    DEBUG = False
    ALLOWED_HOSTS = ['.vercel.app', '.now.sh']
    
    # Agregar whitenoise para archivos estáticos
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
    
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### 4. Crear archivo build_files.sh

```bash
#!/bin/bash

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Aplicar migraciones
python manage.py migrate --noinput
```

### 5. Hacer commit de los cambios

```bash
git add .
git commit -m "feat: configuración para despliegue en Vercel"
git push origin develop
git push origin main
```

### 6. Desplegar en Vercel

1. Ve a https://vercel.com
2. Inicia sesión con GitHub
3. Haz clic en **"Add New Project"**
4. Selecciona tu repositorio
5. Configura:
   - **Framework Preset**: Other
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Output Directory**: (dejar vacío)
6. Haz clic en **"Deploy"**

## 🎯 Resumen de Comandos Importantes

### Comandos de Django

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver

# Recolectar archivos estáticos
python manage.py collectstatic
```

### Comandos de Git

```bash
# Ver estado
git status

# Agregar archivos
git add .

# Hacer commit
git commit -m "mensaje"

# Ver ramas
git branch

# Cambiar de rama
git checkout nombre-rama

# Crear nueva rama
git checkout -b nombre-rama

# Subir cambios
git push origin nombre-rama

# Traer cambios
git pull origin nombre-rama

# Ver historial
git log --oneline
```

## ✅ Checklist Final

### Antes de subir a GitHub:
- [ ] El servidor corre sin errores
- [ ] Puedes crear calificaciones
- [ ] Puedes editar calificaciones
- [ ] Puedes eliminar calificaciones
- [ ] El promedio se calcula automáticamente
- [ ] El promedio general se muestra correctamente
- [ ] El diseño se ve bonito

### Después de subir a GitHub:
- [ ] El repositorio está en GitHub
- [ ] Helen tiene acceso al repositorio
- [ ] La rama `main` existe
- [ ] La rama `develop` existe
- [ ] Tu rama `feature/jiliana-crud` existe

### Después de que Helen termine:
- [ ] Revisaste su Pull Request
- [ ] Hiciste merge de su PR
- [ ] Actualizaste tu repositorio local
- [ ] Probaste todo junto (login + CRUD)
- [ ] Todo funciona correctamente

### Para el despliegue:
- [ ] Instalaste gunicorn y whitenoise
- [ ] Actualizaste requirements.txt
- [ ] Creaste vercel.json
- [ ] Modificaste settings.py para producción
- [ ] Desplegaste en Vercel
- [ ] La aplicación funciona en Vercel

## 🆘 Solución de Problemas

### Error: "Permission denied" al ejecutar git

```bash
# En PowerShell, ejecuta:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Error: "Authentication failed" al hacer push

1. Ve a GitHub → Settings → Developer settings → Personal access tokens
2. Genera un nuevo token
3. Usa el token como contraseña cuando Git te lo pida

### Error: "Port already in use"

```bash
# Detén el servidor con Ctrl+C
# O cambia el puerto:
python manage.py runserver 8001
```

### Error: "No module named django"

```bash
# Activa el entorno virtual primero:
.\venv\Scripts\Activate.ps1

# Luego instala Django:
pip install django
```

## 📞 Ayuda Adicional

Si tienes problemas:
1. Lee el mensaje de error completo
2. Busca en Google el error
3. Revisa la documentación de Django
4. Pregunta en el grupo de clase

¡Mucho éxito! 🚀💜
