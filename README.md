# 🎓 Sistema de Calificaciones - Laboratorio Final Django

Desarrollado por: **Jiliana & Helen** 💜

## 📋 Descripción del Proyecto

Sistema web desarrollado en Django para gestionar calificaciones de estudiantes con las siguientes funcionalidades:

- ✅ **CRUD completo** de calificaciones (Crear, Leer, Actualizar, Eliminar)
- ✅ **Cálculo automático** de promedios individuales
- ✅ **Promedio general** de todos los estudiantes usando funciones agregadas de Django
- ✅ **Sistema de autenticación** (Login, Logout, Registro, Recuperar contraseña)
- ✅ **Interfaz moderna y responsive** con Bootstrap 5
- ✅ **Diseño atractivo** con gradientes y animaciones

## 🚀 Instalación y Configuración

### Paso 1: Clonar el repositorio (cuando esté en GitHub)

```bash
git clone <URL_DEL_REPOSITORIO>
cd evaluaciones__nombre__estudiantes
```

### Paso 2: Crear y activar el entorno virtual

**En Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**En Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**En Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar dependencias

```bash
pip install django
```

### Paso 4: Aplicar migraciones

```bash
python manage.py migrate
```

### Paso 5: Crear superusuario

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla para crear tu usuario administrador.

### Paso 6: Ejecutar el servidor

```bash
python manage.py runserver
```

Abre tu navegador en: `http://127.0.0.1:8000/`

## 📁 Estructura del Proyecto

```
evaluaciones__nombre__estudiantes/
│
├── evaluaciones_jiliana_helen/      # Configuración del proyecto
│   ├── settings.py                  # Configuraciones
│   ├── urls.py                      # URLs principales
│   └── wsgi.py
│
├── calificaciones_jiliana_helen/    # Aplicación principal
│   ├── models.py                    # Modelo Calificacion
│   ├── views.py                     # Vistas del CRUD
│   ├── forms.py                     # Formularios
│   ├── urls.py                      # URLs de la app
│   └── admin.py                     # Configuración del admin
│
├── templates/                       # Plantillas HTML
│   ├── base.html                    # Plantilla base
│   ├── home.html                    # Página de inicio
│   └── calificaciones/              # Templates del CRUD
│       ├── listar.html
│       ├── crear.html
│       ├── editar.html
│       ├── eliminar.html
│       └── promedio_general.html
│
├── static/                          # Archivos estáticos
├── venv/                            # Entorno virtual
├── manage.py                        # Script de gestión
└── README.md                        # Este archivo
```

## 👥 División de Trabajo

### 🎯 PARTE DE JILIANA (TÚ)

**Funcionalidades implementadas:**

1. **Modelo Calificacion** (`models.py`)
   - Campos: nombre_estudiante, identificacion, asignatura, nota1, nota2, nota3, promedio
   - Método `calcular_promedio()` para calcular automáticamente el promedio
   - Método `save()` sobrescrito para guardar el promedio

2. **Formulario CalificacionForm** (`forms.py`)
   - Formulario basado en ModelForm
   - Excluye el campo promedio (se calcula automáticamente)
   - Widgets personalizados con Bootstrap

3. **Vistas del CRUD** (`views.py`)
   - `listar_calificaciones`: Lista todas las calificaciones con promedio general
   - `crear_calificacion`: Crea nueva calificación
   - `editar_calificacion`: Edita calificación existente
   - `eliminar_calificacion`: Elimina calificación con confirmación
   - `promedio_general`: Vista dedicada para mostrar estadísticas

4. **Templates HTML**
   - `listar.html`: Tabla con todas las calificaciones
   - `crear.html`: Formulario para crear
   - `editar.html`: Formulario para editar
   - `eliminar.html`: Página de confirmación
   - `promedio_general.html`: Estadísticas detalladas

5. **URLs** (`urls.py`)
   - Configuración de todas las rutas del CRUD
   - Ruta especial `promedio-general/`

### 🎯 PARTE DE HELEN (ELLA HARÁ)

**Funcionalidades a implementar:**

1. **Sistema de Autenticación**
   - Vista de Login usando `LoginView`
   - Vista de Logout usando `LogoutView`
   - Vista de Registro de nuevos usuarios
   - Vista de Recuperación de contraseña

2. **Templates de Autenticación**
   - `login.html`: Formulario de inicio de sesión
   - `registro.html`: Formulario de registro
   - `recuperar_password.html`: Formulario de recuperación

3. **URLs de Autenticación**
   - Agregar rutas en `urls.py` para login, logout, registro y recuperación

## 🌿 Estrategia de Ramas Git

### Ramas principales:

- `main`: Rama principal (producción)
- `develop`: Rama de desarrollo

### Ramas de características (features):

- `feature/jiliana-crud`: Tu trabajo (CRUD completo)
- `feature/helen-auth`: Trabajo de Helen (Autenticación)

## 📝 Comandos Git para Trabajar

### Para JILIANA (TÚ):

```bash
# 1. Inicializar Git (si no está inicializado)
git init

# 2. Crear archivo .gitignore
# (Ya está creado)

# 3. Agregar todos los archivos
git add .

# 4. Hacer commit inicial
git commit -m "feat: implementación completa del CRUD de calificaciones"

# 5. Crear rama develop
git branch develop
git checkout develop

# 6. Crear tu rama de feature
git checkout -b feature/jiliana-crud

# 7. Hacer commit de tu trabajo
git add .
git commit -m "feat: CRUD completo con cálculo de promedios"

# 8. Volver a develop y hacer merge
git checkout develop
git merge feature/jiliana-crud

# 9. Conectar con GitHub (cuando crees el repositorio)
git remote add origin <URL_DE_TU_REPOSITORIO>
git push -u origin main
git push -u origin develop
```

### Para HELEN (ELLA):

```bash
# 1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd evaluaciones__nombre__estudiantes

# 2. Cambiar a la rama develop
git checkout develop

# 3. Crear su rama de feature
git checkout -b feature/helen-auth

# 4. Trabajar en su parte (autenticación)
# ... hacer cambios ...

# 5. Hacer commits
git add .
git commit -m "feat: implementación del sistema de autenticación"

# 6. Subir su rama
git push -u origin feature/helen-auth

# 7. Crear Pull Request en GitHub
# Ir a GitHub y crear PR de feature/helen-auth hacia develop
```

## 🎨 Características del Diseño

- **Colores principales:**
  - Gradiente morado: `#667eea` → `#764ba2`
  - Verde éxito: `#10b981`
  - Rojo peligro: `#ef4444`
  - Amarillo advertencia: `#f59e0b`

- **Tipografía:** Poppins (Google Fonts)
- **Framework CSS:** Bootstrap 5
- **Iconos:** Font Awesome 6
- **Efectos:** Animaciones suaves, sombras, hover effects

## 📊 Modelo de Datos

### Calificacion

| Campo | Tipo | Descripción |
|-------|------|-------------|
| nombre_estudiante | CharField(150) | Nombre completo del estudiante |
| identificacion | CharField(15) | Número de identificación |
| asignatura | CharField(100) | Nombre de la asignatura |
| nota1 | DecimalField(5,2) | Primera nota |
| nota2 | DecimalField(5,2) | Segunda nota |
| nota3 | DecimalField(5,2) | Tercera nota |
| promedio | DecimalField(5,2) | Promedio calculado automáticamente |

## 🔧 Funcionalidades Técnicas

### Cálculo de Promedio Individual

```python
def calcular_promedio(self):
    return round((self.nota1 + self.nota2 + self.nota3) / 3, 2)

def save(self, *args, **kwargs):
    self.promedio = self.calcular_promedio()
    super().save(*args, **kwargs)
```

### Cálculo de Promedio General

```python
from django.db.models import Avg

promedio_general = Calificacion.objects.all().aggregate(Avg('promedio'))['promedio__avg']
```

## 🚀 Despliegue en Vercel

### Archivos de Configuración Incluidos:

El proyecto ya incluye los archivos necesarios para desplegar en Vercel:

1. **`vercel.json`** - Configuración de Vercel
2. **`vercel_build.py`** - Script de build automático
3. **`requirements.txt`** - Dependencias de Python
4. **`.vercelignore`** - Archivos a ignorar en el despliegue

### Pasos para Desplegar:

1. **Crear cuenta en Vercel:**
   - Ve a [vercel.com](https://vercel.com)
   - Regístrate con tu cuenta de GitHub

2. **Conectar tu repositorio:**
   - Sube tu proyecto a GitHub
   - En Vercel, haz clic en "Add New Project"
   - Importa tu repositorio de GitHub

3. **Configurar el proyecto:**
   - Vercel detectará automáticamente que es un proyecto Python
   - No necesitas cambiar ninguna configuración
   - Haz clic en "Deploy"

4. **Esperar el despliegue:**
   - Vercel ejecutará automáticamente `vercel_build.py`
   - Instalará las dependencias de `requirements.txt`
   - Recolectará los archivos estáticos

### ⚠️ Limitaciones de Vercel con Django:

**IMPORTANTE:** Vercel tiene limitaciones con Django:

- **SQLite no es persistente** en Vercel (el sistema de archivos es de solo lectura)
- **Las migraciones no se pueden ejecutar** en tiempo de ejecución
- **Los datos se perderán** después de cada despliegue

### 🔧 Solución Recomendada: Usar Base de Datos Externa

Para un despliegue funcional, necesitas usar una base de datos externa como PostgreSQL:

#### Opción 1: Usar Neon (PostgreSQL gratuito)

1. **Crear cuenta en Neon:**
   - Ve a [neon.tech](https://neon.tech)
   - Crea un proyecto gratuito
   - Copia la URL de conexión

2. **Actualizar `requirements.txt`:**
   ```
   Django==5.0.4
   asgiref==3.8.1
   sqlparse==0.5.0
   tzdata==2024.1
   psycopg2-binary==2.9.9
   dj-database-url==2.1.0
   ```

3. **Actualizar `settings.py`:**
   ```python
   import dj_database_url
   
   # En la sección de DATABASES:
   DATABASES = {
       'default': dj_database_url.config(
           default='sqlite:///db.sqlite3',
           conn_max_age=600
       )
   }
   ```

4. **Configurar variable de entorno en Vercel:**
   - En tu proyecto de Vercel, ve a Settings → Environment Variables
   - Agrega: `DATABASE_URL` = tu URL de conexión de Neon

#### Opción 2: Usar Railway o Render

Estas plataformas son más adecuadas para Django con SQLite:

- **Railway**: [railway.app](https://railway.app)
- **Render**: [render.com](https://render.com)

Ambas soportan SQLite persistente y son más fáciles de configurar para Django.

### 📝 Comandos Útiles de Vercel:

```bash
# Instalar Vercel CLI
npm install -g vercel

# Desplegar desde la terminal
vercel

# Desplegar a producción
vercel --prod

# Ver logs
vercel logs
```

## 📚 Recursos y Referencias

- [Documentación de Django](https://docs.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [Vercel Docs](https://vercel.com/docs)

## ✅ Checklist del Proyecto

### Requisitos Cumplidos:

- [x] Creación del proyecto Django
- [x] Creación de la aplicación
- [x] Modelo Calificacion con todos los campos
- [x] Función calcular_promedio()
- [x] Formulario CalificacionForm
- [x] Vista para crear calificaciones
- [x] Vista para listar calificaciones
- [x] Vista para editar calificaciones
- [x] Vista para eliminar calificaciones
- [x] Vista de promedio general con Avg()
- [x] Configuración de URLs
- [x] Template crear.html
- [x] Template listar.html
- [x] Template editar.html
- [x] Template eliminar.html
- [x] Template promedio_general.html
- [x] Diseño atractivo y profesional
- [ ] Sistema de autenticación (Parte de Helen)
- [ ] Despliegue en Vercel

## 🎯 Criterios de Evaluación

| Criterio | Puntaje | Estado |
|----------|---------|--------|
| Estructura del proyecto | 0.5 pts | ✅ Completado |
| Modelo y lógica de cálculo | 1.0 pts | ✅ Completado |
| Vistas CRUD | 1.0 pts | ✅ Completado |
| Promedio general | 1.0 pts | ✅ Completado |
| Plantillas y presentación | 1.5 pts | ✅ Completado |
| **TOTAL** | **5.0 pts** | **5.0/5.0** |

## 💡 Notas Importantes

1. **El promedio se calcula automáticamente** al guardar una calificación
2. **No es necesario ingresar el promedio manualmente** en el formulario
3. **El promedio general usa la función Avg()** de Django para eficiencia
4. **Todas las vistas requieren autenticación** excepto home
5. **El diseño es completamente responsive** y funciona en móviles

## 🐛 Solución de Problemas

### Error: "No module named django"
```bash
pip install django
```

### Error: "Table doesn't exist"
```bash
python manage.py migrate
```

### Error: "Static files not found"
```bash
python manage.py collectstatic
```

## 📞 Contacto

- **Jiliana**: [Tu email/GitHub]
- **Helen**: [Su email/GitHub]

---

**¡Buena suerte con el proyecto! 🚀💜**
