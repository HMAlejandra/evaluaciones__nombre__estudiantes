# 📝 Instrucciones para Helen - Sistema de Autenticación

¡Hola Helen! 👋 Aquí están las instrucciones detalladas de lo que debes hacer para completar tu parte del proyecto.

## 🎯 Tu Misión

Implementar el **sistema completo de autenticación** que incluye:

1. ✅ Login (Iniciar Sesión)
2. ✅ Logout (Cerrar Sesión)
3. ✅ Registro de nuevos usuarios
4. ✅ Recuperación de contraseña

## 📋 Pasos a Seguir

### PASO 1: Clonar el repositorio y preparar tu rama

```bash
# 1. Clonar el repositorio (cuando Jiliana lo suba a GitHub)
git clone <URL_DEL_REPOSITORIO>
cd evaluaciones__nombre__estudiantes

# 2. Activar el entorno virtual
# En Windows PowerShell:
.\venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install django

# 4. Aplicar migraciones
python manage.py migrate

# 5. Cambiar a la rama develop
git checkout develop

# 6. Crear tu rama de trabajo
git checkout -b feature/helen-auth
```

### PASO 2: Crear las vistas de autenticación

Abre el archivo `calificaciones_jiliana_helen/views.py` y **AGREGA** al final (no borres nada):

```python

# ============================================
# VISTAS DE AUTENTICACIÓN - PARTE DE HELEN
# ============================================

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth import login
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    """
    Vista personalizada para el inicio de sesión.
    Usa LoginView de Django que maneja todo automáticamente.
    """
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')


class CustomLogoutView(LogoutView):
    """
    Vista personalizada para cerrar sesión.
    Usa LogoutView de Django.
    """
    next_page = 'home'


def registro_view(request):
    """
    Vista para registrar nuevos usuarios.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Bienvenido {user.username}! Tu cuenta ha sido creada exitosamente.')
            return redirect('home')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = UserCreationForm()
    
    return render(request, 'auth/registro.html', {'form': form})


def recuperar_password_view(request):
    """
    Vista para recuperar contraseña.
    """
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=False,
                email_template_name='auth/password_reset_email.html',
            )
            messages.success(request, 'Se ha enviado un correo con instrucciones para recuperar tu contraseña.')
            return redirect('login')
    else:
        form = PasswordResetForm()
    
    return render(request, 'auth/recuperar_password.html', {'form': form})
```

### PASO 3: Actualizar las URLs

Abre el archivo `calificaciones_jiliana_helen/urls.py` y **REEMPLAZA** las líneas comentadas por:

```python
    # URLs de autenticación - PARTE DE HELEN
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('recuperar-password/', views.recuperar_password_view, name='recuperar_password'),
```

### PASO 4: Crear los templates de autenticación

#### 4.1 Crear `templates/auth/login.html`

```html
{% extends 'base.html' %}

{% block title %}Iniciar Sesión{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-5">
        <h1 class="page-title text-center mb-4">
            <i class="fas fa-sign-in-alt"></i> Iniciar Sesión
        </h1>
        
        <div class="card">
            <div class="card-body p-4">
                <form method="post" novalidate>
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="id_username" class="form-label">
                            <i class="fas fa-user"></i> Usuario
                        </label>
                        <input type="text" 
                               name="username" 
                               class="form-control" 
                               id="id_username" 
                               placeholder="Ingresa tu usuario"
                               required>
                    </div>
                    
                    <div class="mb-3">
                        <label for="id_password" class="form-label">
                            <i class="fas fa-lock"></i> Contraseña
                        </label>
                        <input type="password" 
                               name="password" 
                               class="form-control" 
                               id="id_password" 
                               placeholder="Ingresa tu contraseña"
                               required>
                    </div>
                    
                    {% if form.errors %}
                    <div class="alert alert-danger" role="alert">
                        <i class="fas fa-exclamation-circle"></i> 
                        Usuario o contraseña incorrectos.
                    </div>
                    {% endif %}
                    
                    <div class="d-grid gap-2 mb-3">
                        <button type="submit" class="btn btn-primary btn-lg">
                            <i class="fas fa-sign-in-alt"></i> Iniciar Sesión
                        </button>
                    </div>
                    
                    <div class="text-center">
                        <p class="mb-2">
                            <a href="{% url 'recuperar_password' %}" class="text-decoration-none">
                                <i class="fas fa-key"></i> ¿Olvidaste tu contraseña?
                            </a>
                        </p>
                        <p class="mb-0">
                            ¿No tienes cuenta? 
                            <a href="{% url 'registro' %}" class="text-decoration-none">
                                <i class="fas fa-user-plus"></i> Regístrate aquí
                            </a>
                        </p>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

#### 4.2 Crear `templates/auth/registro.html`

```html
{% extends 'base.html' %}

{% block title %}Registro{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <h1 class="page-title text-center mb-4">
            <i class="fas fa-user-plus"></i> Crear Cuenta Nueva
        </h1>
        
        <div class="card">
            <div class="card-body p-4">
                <form method="post" novalidate>
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="{{ form.username.id_for_label }}" class="form-label">
                            <i class="fas fa-user"></i> {{ form.username.label }}
                        </label>
                        {{ form.username }}
                        {% if form.username.errors %}
                            <div class="text-danger mt-1">
                                {{ form.username.errors }}
                            </div>
                        {% else %}
                            <small class="text-muted">
                                150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.
                            </small>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.password1.id_for_label }}" class="form-label">
                            <i class="fas fa-lock"></i> {{ form.password1.label }}
                        </label>
                        {{ form.password1 }}
                        {% if form.password1.errors %}
                            <div class="text-danger mt-1">
                                {{ form.password1.errors }}
                            </div>
                        {% else %}
                            <small class="text-muted">
                                Tu contraseña debe tener al menos 8 caracteres.
                            </small>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.password2.id_for_label }}" class="form-label">
                            <i class="fas fa-lock"></i> {{ form.password2.label }}
                        </label>
                        {{ form.password2 }}
                        {% if form.password2.errors %}
                            <div class="text-danger mt-1">
                                {{ form.password2.errors }}
                            </div>
                        {% else %}
                            <small class="text-muted">
                                Ingresa la misma contraseña para verificación.
                            </small>
                        {% endif %}
                    </div>
                    
                    <div class="d-grid gap-2 mb-3">
                        <button type="submit" class="btn btn-success btn-lg">
                            <i class="fas fa-user-plus"></i> Crear Cuenta
                        </button>
                    </div>
                    
                    <div class="text-center">
                        <p class="mb-0">
                            ¿Ya tienes cuenta? 
                            <a href="{% url 'login' %}" class="text-decoration-none">
                                <i class="fas fa-sign-in-alt"></i> Inicia sesión aquí
                            </a>
                        </p>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<style>
    input[type="text"], input[type="password"] {
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        padding: 0.75rem;
    }
    
    input[type="text"]:focus, input[type="password"]:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
    }
</style>
{% endblock %}
```

#### 4.3 Crear `templates/auth/recuperar_password.html`

```html
{% extends 'base.html' %}

{% block title %}Recuperar Contraseña{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-5">
        <h1 class="page-title text-center mb-4">
            <i class="fas fa-key"></i> Recuperar Contraseña
        </h1>
        
        <div class="card">
            <div class="card-body p-4">
                <div class="alert alert-info" role="alert">
                    <i class="fas fa-info-circle"></i> 
                    Ingresa tu correo electrónico y te enviaremos instrucciones para recuperar tu contraseña.
                </div>
                
                <form method="post" novalidate>
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="{{ form.email.id_for_label }}" class="form-label">
                            <i class="fas fa-envelope"></i> Correo Electrónico
                        </label>
                        <input type="email" 
                               name="email" 
                               class="form-control" 
                               id="id_email" 
                               placeholder="tu@email.com"
                               required>
                        {% if form.email.errors %}
                            <div class="text-danger mt-1">
                                {{ form.email.errors }}
                            </div>
                        {% endif %}
                    </div>
                    
                    <div class="d-grid gap-2 mb-3">
                        <button type="submit" class="btn btn-primary btn-lg">
                            <i class="fas fa-paper-plane"></i> Enviar Instrucciones
                        </button>
                    </div>
                    
                    <div class="text-center">
                        <p class="mb-0">
                            <a href="{% url 'login' %}" class="text-decoration-none">
                                <i class="fas fa-arrow-left"></i> Volver al inicio de sesión
                            </a>
                        </p>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

#### 4.4 Crear `templates/auth/password_reset_email.html`

```html
Hola,

Has solicitado recuperar tu contraseña en el Sistema de Calificaciones.

Por favor, haz clic en el siguiente enlace para crear una nueva contraseña:

{{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}

Si no solicitaste este cambio, puedes ignorar este correo.

Saludos,
El equipo del Sistema de Calificaciones
```

### PASO 5: Actualizar el navbar en base.html

Abre `templates/base.html` y **REEMPLAZA** las líneas del navbar que tienen `href="#"` por las URLs correctas:

```html
<!-- Cambiar estas líneas: -->
<a class="nav-link" href="#">
    <i class="fas fa-sign-out-alt"></i> Cerrar Sesión
</a>

<!-- Por: -->
<a class="nav-link" href="{% url 'logout' %}">
    <i class="fas fa-sign-out-alt"></i> Cerrar Sesión
</a>

<!-- Y cambiar: -->
<a class="nav-link" href="#">
    <i class="fas fa-sign-in-alt"></i> Iniciar Sesión
</a>

<!-- Por: -->
<a class="nav-link" href="{% url 'login' %}">
    <i class="fas fa-sign-in-alt"></i> Iniciar Sesión
</a>

<!-- Y cambiar: -->
<a class="nav-link" href="#">
    <i class="fas fa-user-plus"></i> Registrarse
</a>

<!-- Por: -->
<a class="nav-link" href="{% url 'registro' %}">
    <i class="fas fa-user-plus"></i> Registrarse
</a>
```

### PASO 6: Probar tu trabajo

```bash
# 1. Ejecutar el servidor
python manage.py runserver

# 2. Probar en el navegador:
# - http://127.0.0.1:8000/login/
# - http://127.0.0.1:8000/registro/
# - http://127.0.0.1:8000/recuperar-password/
# - http://127.0.0.1:8000/logout/
```

### PASO 7: Hacer commit y push

```bash
# 1. Ver los cambios
git status

# 2. Agregar todos los archivos
git add .

# 3. Hacer commit
git commit -m "feat: implementación completa del sistema de autenticación"

# 4. Subir tu rama
git push -u origin feature/helen-auth
```

### PASO 8: Crear Pull Request

1. Ve a GitHub
2. Verás un botón que dice "Compare & pull request"
3. Haz clic en él
4. Asegúrate de que el PR sea de `feature/helen-auth` hacia `develop`
5. Escribe un título: "Implementación del sistema de autenticación"
6. Describe lo que hiciste
7. Haz clic en "Create pull request"
8. Avísale a Jiliana para que revise y apruebe el PR

## ✅ Checklist de tu trabajo

- [ ] Clonar el repositorio
- [ ] Crear rama feature/helen-auth
- [ ] Agregar vistas de autenticación en views.py
- [ ] Actualizar URLs en urls.py
- [ ] Crear template login.html
- [ ] Crear template registro.html
- [ ] Crear template recuperar_password.html
- [ ] Crear template password_reset_email.html
- [ ] Actualizar enlaces en base.html
- [ ] Probar todas las funcionalidades
- [ ] Hacer commit y push
- [ ] Crear Pull Request

## 💡 Conceptos Importantes

### ¿Qué es LoginView?

`LoginView` es una vista basada en clases que Django proporciona para manejar el inicio de sesión. Hace todo el trabajo pesado por ti:
- Muestra el formulario de login
- Valida las credenciales
- Inicia la sesión del usuario
- Redirige al usuario después del login

### ¿Qué es LogoutView?

`LogoutView` es similar pero para cerrar sesión. Cierra la sesión del usuario y lo redirige a donde le indiques.

### ¿Por qué usar estas vistas?

Porque Django ya las tiene probadas y son seguras. No necesitas escribir todo el código desde cero.

## 🆘 Si tienes problemas

1. **Error de importación**: Asegúrate de haber agregado los imports al inicio de views.py
2. **Template no encontrado**: Verifica que creaste la carpeta `templates/auth/`
3. **URL no funciona**: Revisa que el nombre en `urls.py` coincida con el que usas en los templates

## 📞 Contacto

Si tienes dudas, pregúntale a Jiliana o revisa la documentación de Django:
- https://docs.djangoproject.com/en/stable/topics/auth/

¡Mucho éxito! 🚀💜
