# 🏗️ Arquitectura Visual del Proyecto

## 📊 Diagrama de Flujo del Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                        USUARIO                               │
│                     (Navegador Web)                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    DJANGO URLS                               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  /                          → home                    │  │
│  │  /calificaciones/           → listar_calificaciones   │  │
│  │  /calificaciones/crear/     → crear_calificacion      │  │
│  │  /calificaciones/editar/id/ → editar_calificacion     │  │
│  │  /calificaciones/eliminar/  → eliminar_calificacion   │  │
│  │  /promedio-general/         → promedio_general        │  │
│  │  /admin/                    → Django Admin            │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    DJANGO VIEWS                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  home()                                               │  │
│  │  listar_calificaciones()                              │  │
│  │  crear_calificacion()                                 │  │
│  │  editar_calificacion()                                │  │
│  │  eliminar_calificacion()                              │  │
│  │  promedio_general()                                   │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────┬───────────────────────────┬────────────────────┘
             │                           │
             ▼                           ▼
┌────────────────────────┐  ┌───────────────────────────────┐
│   DJANGO FORMS         │  │     DJANGO MODELS             │
│  ┌──────────────────┐  │  │  ┌─────────────────────────┐ │
│  │ CalificacionForm │  │  │  │  Calificacion           │ │
│  │  - nombre        │  │  │  │   - nombre_estudiante   │ │
│  │  - identificacion│  │  │  │   - identificacion      │ │
│  │  - asignatura    │  │  │  │   - asignatura          │ │
│  │  - nota1         │  │  │  │   - nota1               │ │
│  │  - nota2         │  │  │  │   - nota2               │ │
│  │  - nota3         │  │  │  │   - nota3               │ │
│  └──────────────────┘  │  │  │   - promedio (auto)     │ │
└────────────────────────┘  │  │                         │ │
                            │  │  calcular_promedio()    │ │
                            │  │  save()                 │ │
                            │  └─────────────────────────┘ │
                            └───────────────┬───────────────┘
                                            │
                                            ▼
                            ┌───────────────────────────────┐
                            │      BASE DE DATOS            │
                            │       (SQLite3)               │
                            │  ┌─────────────────────────┐ │
                            │  │  Tabla: Calificacion    │ │
                            │  │  - id                   │ │
                            │  │  - nombre_estudiante    │ │
                            │  │  - identificacion       │ │
                            │  │  - asignatura           │ │
                            │  │  - nota1                │ │
                            │  │  - nota2                │ │
                            │  │  - nota3                │ │
                            │  │  - promedio             │ │
                            │  └─────────────────────────┘ │
                            └───────────────────────────────┘
```

## 🎨 Flujo de Creación de Calificación

```
USUARIO                    DJANGO                      BASE DE DATOS
   │                          │                              │
   │  1. Abre formulario      │                              │
   ├─────────────────────────>│                              │
   │                          │                              │
   │  2. Muestra formulario   │                              │
   │<─────────────────────────┤                              │
   │                          │                              │
   │  3. Llena y envía datos  │                              │
   ├─────────────────────────>│                              │
   │                          │                              │
   │                          │  4. Valida datos             │
   │                          │                              │
   │                          │  5. Calcula promedio         │
   │                          │     (nota1+nota2+nota3)/3    │
   │                          │                              │
   │                          │  6. Guarda en BD             │
   │                          ├─────────────────────────────>│
   │                          │                              │
   │                          │  7. Confirmación             │
   │                          │<─────────────────────────────┤
   │                          │                              │
   │  8. Mensaje de éxito     │                              │
   │<─────────────────────────┤                              │
   │                          │                              │
   │  9. Redirige a lista     │                              │
   │<─────────────────────────┤                              │
   │                          │                              │
```

## 📁 Estructura de Archivos

```
evaluaciones__nombre__estudiantes/
│
├── 📂 evaluaciones_jiliana_helen/    # Configuración del proyecto
│   ├── ⚙️ settings.py                # Configuraciones
│   ├── 🔗 urls.py                    # URLs principales
│   ├── 🚀 wsgi.py                    # Servidor WSGI
│   └── 🔧 asgi.py                    # Servidor ASGI
│
├── 📂 calificaciones_jiliana_helen/  # Aplicación principal
│   ├── 📂 migrations/                # Migraciones de BD
│   │   └── 0001_initial.py
│   ├── 🗄️ models.py                  # Modelo Calificacion
│   ├── 👁️ views.py                   # 6 vistas (CRUD + home + promedio)
│   ├── 📝 forms.py                   # CalificacionForm
│   ├── 🔗 urls.py                    # URLs de la app
│   └── ⚙️ admin.py                   # Configuración admin
│
├── 📂 templates/                     # Plantillas HTML
│   ├── 📄 base.html                  # Plantilla base
│   ├── 🏠 home.html                  # Página de inicio
│   └── 📂 calificaciones/
│       ├── 📋 listar.html            # Lista de calificaciones
│       ├── ➕ crear.html             # Formulario crear
│       ├── ✏️ editar.html            # Formulario editar
│       ├── 🗑️ eliminar.html          # Confirmación eliminar
│       └── 📊 promedio_general.html  # Estadísticas
│
├── 📂 static/                        # Archivos estáticos (CSS, JS, imágenes)
├── 📂 venv/                          # Entorno virtual
│
├── 📄 manage.py                      # Script de gestión Django
├── 📄 db.sqlite3                     # Base de datos
├── 📄 requirements.txt               # Dependencias
├── 📄 .gitignore                     # Archivos ignorados por Git
│
├── 📚 README.md                      # Documentación principal
├── 📚 TUTORIAL_PASO_A_PASO.md        # Tutorial para principiantes
├── 📚 COMANDOS_JILIANA.md            # Comandos para Jiliana
├── 📚 INSTRUCCIONES_HELEN.md         # Instrucciones para Helen
├── 📚 RESUMEN_PROYECTO.md            # Resumen técnico
├── 📚 INICIO_RAPIDO.md               # Guía de inicio rápido
└── 📚 ARQUITECTURA_VISUAL.md         # Este archivo
```

## 🔄 Ciclo de Vida de una Petición

```
1. USUARIO escribe URL
   ↓
2. DJANGO recibe la petición
   ↓
3. URLS.PY busca la ruta correspondiente
   ↓
4. VIEWS.PY ejecuta la función correspondiente
   ↓
5. Si es necesario, consulta MODELS.PY
   ↓
6. MODELS.PY consulta la BASE DE DATOS
   ↓
7. BASE DE DATOS devuelve los datos
   ↓
8. VIEWS.PY procesa los datos
   ↓
9. VIEWS.PY renderiza el TEMPLATE
   ↓
10. TEMPLATE genera HTML
   ↓
11. DJANGO envía HTML al navegador
   ↓
12. USUARIO ve la página
```

## 🎯 Patrón MVT de Django

```
┌─────────────────────────────────────────────────────────┐
│                    PATRÓN MVT                            │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────┐      ┌──────────┐      ┌──────────┐     │
│  │  MODEL   │      │   VIEW   │      │ TEMPLATE │     │
│  │          │      │          │      │          │     │
│  │ models.py│◄────►│ views.py │◄────►│ *.html   │     │
│  │          │      │          │      │          │     │
│  │ Define   │      │ Lógica   │      │ Presenta │     │
│  │ datos    │      │ negocio  │      │ datos    │     │
│  └────┬─────┘      └──────────┘      └──────────┘     │
│       │                                                 │
│       ▼                                                 │
│  ┌──────────┐                                          │
│  │   BASE   │                                          │
│  │   DATOS  │                                          │
│  └──────────┘                                          │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

## 🧮 Cálculo de Promedios

### Promedio Individual

```
┌─────────────────────────────────────────┐
│  ENTRADA                                 │
│  - Nota 1: 85                           │
│  - Nota 2: 90                           │
│  - Nota 3: 88                           │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  PROCESO                                 │
│  promedio = (85 + 90 + 88) / 3          │
│  promedio = 263 / 3                     │
│  promedio = 87.666...                   │
│  promedio = round(87.666..., 2)         │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  SALIDA                                  │
│  Promedio: 87.67                        │
└─────────────────────────────────────────┘
```

### Promedio General

```
┌─────────────────────────────────────────┐
│  ENTRADA (Base de Datos)                 │
│  - Estudiante 1: promedio = 87.67       │
│  - Estudiante 2: promedio = 77.67       │
│  - Estudiante 3: promedio = 92.33       │
│  - Estudiante 4: promedio = 72.33       │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  PROCESO (Django Avg)                    │
│  from django.db.models import Avg       │
│  promedio_general = Calificacion        │
│    .objects.all()                       │
│    .aggregate(Avg('promedio'))          │
│    ['promedio__avg']                    │
│                                          │
│  = (87.67 + 77.67 + 92.33 + 72.33) / 4 │
│  = 330 / 4                              │
│  = 82.50                                │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  SALIDA                                  │
│  Promedio General: 82.50                │
└─────────────────────────────────────────┘
```

## 🎨 Componentes del Diseño

```
┌─────────────────────────────────────────────────────────┐
│                      NAVBAR                              │
│  Logo | Inicio | Calificaciones | Nueva | Promedio      │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                    MENSAJES                              │
│  ✅ ¡Calificación creada exitosamente!                  │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                  CONTENIDO PRINCIPAL                     │
│                                                          │
│  ┌────────────────────────────────────────────────┐    │
│  │              TARJETAS / TABLAS                  │    │
│  │                                                 │    │
│  │  [Card 1]  [Card 2]  [Card 3]                  │    │
│  │                                                 │    │
│  │  ┌──────────────────────────────────────┐     │    │
│  │  │         TABLA DE DATOS               │     │    │
│  │  │  Nombre | Notas | Promedio | Acciones│     │    │
│  │  └──────────────────────────────────────┘     │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                      FOOTER                              │
│  Desarrollado por Jiliana & Helen 💜                    │
└─────────────────────────────────────────────────────────┘
```

## 🔐 Sistema de Autenticación (Pendiente - Helen)

```
┌─────────────────────────────────────────────────────────┐
│                  AUTENTICACIÓN                           │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐    ┌──────────────┐                  │
│  │    LOGIN     │    │   LOGOUT     │                  │
│  │              │    │              │                  │
│  │ LoginView    │    │ LogoutView   │                  │
│  │ (Django)     │    │ (Django)     │                  │
│  └──────────────┘    └──────────────┘                  │
│                                                          │
│  ┌──────────────┐    ┌──────────────┐                  │
│  │   REGISTRO   │    │  RECUPERAR   │                  │
│  │              │    │  PASSWORD    │                  │
│  │ Custom View  │    │ Custom View  │                  │
│  └──────────────┘    └──────────────┘                  │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

## 🌐 Flujo de Trabajo Git

```
MAIN (Producción)
  │
  ├─── DEVELOP (Desarrollo)
  │      │
  │      ├─── feature/jiliana-crud (Tu trabajo)
  │      │      │
  │      │      ├─ Modelo
  │      │      ├─ Vistas
  │      │      ├─ Forms
  │      │      ├─ Templates
  │      │      └─ URLs
  │      │
  │      └─── feature/helen-auth (Trabajo de Helen)
  │             │
  │             ├─ LoginView
  │             ├─ LogoutView
  │             ├─ Registro
  │             └─ Recuperar Password
  │
  └─── Merge final → MAIN
```

## 📊 Estadísticas del Proyecto

```
┌─────────────────────────────────────────┐
│         ESTADÍSTICAS                     │
├─────────────────────────────────────────┤
│  📄 Archivos Python:        6           │
│  📄 Templates HTML:         7           │
│  📄 Vistas creadas:         6           │
│  📄 URLs configuradas:      6           │
│  📄 Modelos:                1           │
│  📄 Formularios:            1           │
│  📄 Líneas de código:       ~1000+      │
│  📄 Archivos de docs:       7           │
└─────────────────────────────────────────┘
```

## 🎯 Tecnologías Utilizadas

```
┌─────────────────────────────────────────────────────────┐
│                    STACK TECNOLÓGICO                     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  BACKEND                                                 │
│  ├─ Django 6.0.4                                        │
│  ├─ Python 3.13.7                                       │
│  └─ SQLite3                                             │
│                                                          │
│  FRONTEND                                                │
│  ├─ HTML5                                               │
│  ├─ CSS3                                                │
│  ├─ Bootstrap 5.3.0                                     │
│  ├─ Font Awesome 6.4.0                                  │
│  └─ Google Fonts (Poppins)                              │
│                                                          │
│  HERRAMIENTAS                                            │
│  ├─ Git                                                 │
│  ├─ GitHub                                              │
│  └─ Vercel (para despliegue)                            │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

**Este diagrama te ayuda a visualizar cómo funciona todo el sistema. 🎨**

**¡Ahora entiendes la arquitectura completa! 🏗️✨**
