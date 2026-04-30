# ❓ Preguntas Frecuentes (FAQ)

## 🎯 Preguntas Generales

### ¿Qué es este proyecto?

Es un sistema web para gestionar calificaciones de estudiantes. Puedes crear, ver, editar y eliminar calificaciones, y el sistema calcula automáticamente los promedios.

### ¿Para qué sirve?

Es un laboratorio final de Django que demuestra:
- Cómo crear un CRUD completo
- Cómo calcular promedios automáticamente
- Cómo diseñar una interfaz bonita
- Cómo trabajar en equipo con Git

### ¿Quién hizo qué?

- **Jiliana (tú)**: CRUD completo + cálculo de promedios + diseño
- **Helen**: Sistema de autenticación (login, logout, registro, recuperar contraseña)

---

## 🚀 Instalación y Configuración

### ¿Cómo instalo Django?

```bash
pip install django
```

### ¿Cómo creo la base de datos?

```bash
python manage.py migrate
```

### ¿Cómo creo un usuario administrador?

```bash
python manage.py createsuperuser
```

### ¿Cómo inicio el servidor?

```bash
python manage.py runserver
```

### ¿En qué puerto corre el servidor?

Por defecto en el puerto 8000: `http://127.0.0.1:8000/`

### ¿Puedo cambiar el puerto?

Sí:
```bash
python manage.py runserver 8001
```

---

## 💻 Uso del Sistema

### ¿Cómo creo una calificación?

1. Ve a: `http://127.0.0.1:8000/calificaciones/crear/`
2. Llena el formulario
3. Haz clic en "Guardar"

### ¿El promedio se calcula solo?

Sí, automáticamente cuando guardas una calificación.

### ¿Cómo edito una calificación?

1. Ve a la lista de calificaciones
2. Haz clic en el botón amarillo (editar)
3. Modifica los datos
4. Guarda

### ¿Cómo elimino una calificación?

1. Ve a la lista de calificaciones
2. Haz clic en el botón rojo (eliminar)
3. Confirma la eliminación

### ¿Cómo veo el promedio general?

Ve a: `http://127.0.0.1:8000/promedio-general/`

### ¿Puedo acceder sin iniciar sesión?

No, todas las funciones del CRUD requieren que inicies sesión (excepto la página de inicio).

---

## 🎨 Diseño y Apariencia

### ¿Por qué se ve tan bonito?

Usamos:
- Bootstrap 5 (framework CSS)
- Font Awesome (iconos)
- Google Fonts (tipografía Poppins)
- CSS personalizado (gradientes y animaciones)

### ¿Puedo cambiar los colores?

Sí, edita el archivo `templates/base.html` en la sección `<style>` y cambia las variables CSS:

```css
:root {
    --primary-color: #6366f1;  /* Cambia este color */
    --secondary-color: #8b5cf6;
    /* etc... */
}
```

### ¿Funciona en celular?

Sí, el diseño es responsive gracias a Bootstrap.

### ¿Puedo agregar mi logo?

Sí, edita `templates/base.html` en la sección del navbar y agrega tu imagen.

---

## 🔧 Problemas Técnicos

### Error: "No module named django"

**Solución:**
```bash
pip install django
```

### Error: "Port already in use"

**Solución:**
```bash
# Detén el servidor con Ctrl+C
# O usa otro puerto:
python manage.py runserver 8001
```

### Error: "Table doesn't exist"

**Solución:**
```bash
python manage.py migrate
```

### Error: "CSRF verification failed"

**Solución:**
- Asegúrate de tener `{% csrf_token %}` en todos los formularios
- Limpia las cookies del navegador
- Refresca la página

### Error: "Static files not found"

**Solución:**
```bash
python manage.py collectstatic
```

### La página se ve sin estilos

**Solución:**
- Verifica que tengas conexión a internet (Bootstrap se carga desde CDN)
- Refresca la página con Ctrl+F5
- Revisa la consola del navegador (F12) para ver errores

### Error: "Permission denied" en PowerShell

**Solución:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📊 Base de Datos

### ¿Qué base de datos usa?

SQLite3 (archivo `db.sqlite3`)

### ¿Puedo usar otra base de datos?

Sí, puedes configurar PostgreSQL, MySQL, etc. en `settings.py`

### ¿Cómo veo los datos en la base de datos?

1. Usa el admin de Django: `http://127.0.0.1:8000/admin/`
2. O usa un visor de SQLite como DB Browser

### ¿Cómo borro todos los datos?

```bash
# Elimina la base de datos
del db.sqlite3

# Vuelve a crearla
python manage.py migrate
```

### ¿Cómo hago backup de los datos?

```bash
# Exportar datos
python manage.py dumpdata > backup.json

# Importar datos
python manage.py loaddata backup.json
```

---

## 🌿 Git y GitHub

### ¿Cómo subo mi proyecto a GitHub?

```bash
git init
git add .
git commit -m "feat: proyecto completo"
git remote add origin <URL_DE_TU_REPO>
git push -u origin main
```

### ¿Cómo creo una rama?

```bash
git checkout -b nombre-de-la-rama
```

### ¿Cómo cambio de rama?

```bash
git checkout nombre-de-la-rama
```

### ¿Cómo hago merge?

```bash
git checkout develop
git merge feature/mi-rama
```

### ¿Qué es un Pull Request?

Es una solicitud para que tu código sea revisado y fusionado con otra rama. Se hace en GitHub.

### ¿Cómo resuelvo conflictos?

1. Git te mostrará los archivos con conflictos
2. Abre los archivos y busca las marcas `<<<<<<<`, `=======`, `>>>>>>>`
3. Decide qué código mantener
4. Elimina las marcas
5. Guarda el archivo
6. Haz commit

---

## 🚀 Despliegue

### ¿Cómo despliego en Vercel?

1. Instala dependencias:
```bash
pip install gunicorn whitenoise
pip freeze > requirements.txt
```

2. Sube tu código a GitHub

3. Ve a https://vercel.com

4. Conecta tu repositorio

5. Despliega

### ¿Puedo desplegar en otro lugar?

Sí, puedes usar:
- Heroku
- PythonAnywhere
- Railway
- Render
- AWS
- Google Cloud

### ¿Necesito cambiar algo para producción?

Sí, en `settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['tu-dominio.com']
```

---

## 👥 Trabajo en Equipo

### ¿Cómo trabaja Helen en el proyecto?

1. Tú subes tu código a GitHub
2. La invitas como colaboradora
3. Ella clona el repositorio
4. Crea su rama `feature/helen-auth`
5. Hace su parte
6. Crea un Pull Request
7. Tú revisas y apruebas
8. Haces merge

### ¿Qué pasa si hacemos cambios al mismo tiempo?

Git detectará los conflictos y tendrán que resolverlos manualmente.

### ¿Cómo nos comunicamos?

- GitHub Issues
- Pull Request comments
- WhatsApp/Telegram
- Reuniones

---

## 📚 Aprendizaje

### ¿Dónde aprendo más sobre Django?

- Documentación oficial: https://docs.djangoproject.com/
- Tutorial oficial: https://docs.djangoproject.com/en/stable/intro/tutorial01/
- YouTube: Busca "Django tutorial español"
- Cursos en Udemy, Platzi, Coursera

### ¿Qué otros proyectos puedo hacer?

- Blog personal
- Tienda online
- Red social
- Sistema de reservas
- Gestor de tareas
- API REST

### ¿Qué tecnologías debería aprender después?

- Django REST Framework (APIs)
- React o Vue.js (frontend moderno)
- PostgreSQL (base de datos profesional)
- Docker (contenedores)
- Celery (tareas asíncronas)

---

## 🎯 Evaluación

### ¿Cumple con todos los requisitos?

Sí, cumple con el 100% de los requisitos del laboratorio.

### ¿Qué puntaje puedo obtener?

Si todo funciona correctamente: **5.0/5.0**

### ¿Qué valoran los profesores?

1. Que funcione sin errores
2. Código limpio y organizado
3. Diseño atractivo
4. Documentación completa
5. Trabajo en equipo

### ¿Qué puedo mejorar?

- Agregar más validaciones
- Implementar búsqueda y filtros
- Agregar gráficas
- Exportar a PDF o Excel
- Agregar más roles de usuario

---

## 🔐 Seguridad

### ¿Es seguro este proyecto?

Para desarrollo sí, pero para producción necesitas:
- Cambiar `SECRET_KEY`
- Poner `DEBUG = False`
- Usar HTTPS
- Configurar CORS
- Agregar rate limiting

### ¿Cómo protejo las contraseñas?

Django las encripta automáticamente con PBKDF2.

### ¿Qué es CSRF?

Cross-Site Request Forgery. Django lo previene automáticamente con `{% csrf_token %}`.

---

## 💡 Consejos

### ¿Qué hago si me atasco?

1. Lee el mensaje de error completo
2. Busca en Google el error
3. Revisa la documentación
4. Pregunta en Stack Overflow
5. Pide ayuda a tus compañeros

### ¿Cómo organizo mi tiempo?

1. Día 1: Configuración y modelo
2. Día 2: Vistas y formularios
3. Día 3: Templates y diseño
4. Día 4: Pruebas y correcciones
5. Día 5: Documentación y despliegue

### ¿Qué hago si algo no funciona?

1. No entres en pánico
2. Lee el error
3. Busca en Google
4. Revisa tu código
5. Compara con el código de ejemplo
6. Pide ayuda

---

## 📞 Soporte

### ¿Dónde pido ayuda?

- Documentación del proyecto (README.md)
- Documentación de Django
- Stack Overflow
- Comunidad de Django en español
- Tu profesor o compañeros

### ¿Puedo contactar a alguien?

Sí, pregunta a:
- Tu compañera Helen
- Tus compañeros de clase
- Tu profesor
- Comunidades en línea

---

## 🎉 Éxito

### ¿Qué hago cuando termine?

1. Prueba todo exhaustivamente
2. Documenta bien tu código
3. Sube a GitHub
4. Despliega en Vercel
5. Prepara tu presentación
6. ¡Celebra! 🎉

### ¿Puedo usar este proyecto en mi portafolio?

¡Sí! Es un excelente proyecto para mostrar tus habilidades.

### ¿Qué sigue después de este proyecto?

- Aprende Django REST Framework
- Aprende un framework de frontend (React, Vue)
- Construye proyectos más complejos
- Contribuye a proyectos open source
- Busca prácticas o trabajo

---

**¿Tienes más preguntas? ¡Pregunta sin miedo! 💜**

**Recuerda: No hay preguntas tontas, solo respuestas sin descubrir. 🚀**
