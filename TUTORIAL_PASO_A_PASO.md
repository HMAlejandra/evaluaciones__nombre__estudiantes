# 🎓 Tutorial Paso a Paso - Como si fueras una niña de primaria

## 🌟 ¿Qué vamos a hacer?

Imagina que tienes una libreta donde anotas las calificaciones de tus compañeros. Pero en lugar de usar papel, vamos a crear una página web donde puedes:

- ✏️ Escribir las calificaciones
- 👀 Ver todas las calificaciones
- ✨ Cambiar las calificaciones si te equivocaste
- 🗑️ Borrar calificaciones
- 🧮 Ver el promedio de todos

## 📚 Paso 1: Entender qué ya tienes

Ya tienes TODO listo en tu computadora. Es como si ya tuvieras la libreta, los lápices y las hojas. Solo falta que empieces a usarlos.

### ¿Qué archivos importantes tienes?

1. **manage.py** - Es como el director de la escuela, controla todo
2. **models.py** - Es donde defines cómo se ve una calificación (nombre, notas, etc.)
3. **views.py** - Son las acciones que puedes hacer (crear, ver, editar, borrar)
4. **templates/** - Son las páginas bonitas que ves en el navegador
5. **urls.py** - Son las direcciones de cada página

## 🚀 Paso 2: Encender tu proyecto

### 2.1 Abrir la terminal

1. Presiona las teclas `Windows + R`
2. Escribe `cmd` y presiona Enter
3. Te aparecerá una ventana negra (la terminal)

### 2.2 Ir a tu carpeta del proyecto

```bash
cd Documents\evaluaciones__nombre__estudiantes
```

**¿Qué significa esto?**
- `cd` = "Change Directory" = "Cambiar de carpeta"
- Es como decirle a la computadora: "Ve a esta carpeta"

### 2.3 Activar el entorno virtual

```bash
venv\Scripts\activate
```

**¿Qué es el entorno virtual?**
- Es como una burbuja mágica donde vive tu proyecto
- Dentro de esta burbuja tienes todo lo que necesitas (Django, etc.)
- Cuando lo activas, verás `(venv)` al inicio de la línea

### 2.4 Crear la base de datos

```bash
python manage.py migrate
```

**¿Qué hace esto?**
- Crea una base de datos (como una libreta digital)
- Prepara las tablas donde se guardarán las calificaciones
- Es como preparar las hojas de tu libreta con renglones

### 2.5 Crear tu usuario administrador

```bash
python manage.py createsuperuser
```

**Te preguntará:**

1. **Username**: Escribe tu nombre (ejemplo: `jiliana`)
2. **Email**: Puedes dejarlo en blanco (solo presiona Enter)
3. **Password**: Escribe una contraseña (no se verá mientras escribes, es normal)
4. **Password (again)**: Escribe la misma contraseña otra vez

**¡Importante!** Anota tu usuario y contraseña en un papel, los necesitarás después.

### 2.6 Encender el servidor

```bash
python manage.py runserver
```

**¿Qué hace esto?**
- Enciende tu página web
- Es como abrir tu tienda para que la gente pueda entrar
- Verás algo como: `Starting development server at http://127.0.0.1:8000/`

**¡NO CIERRES ESTA VENTANA!** Déjala abierta mientras trabajas.

## 🌐 Paso 3: Ver tu página web

### 3.1 Abrir el navegador

1. Abre Google Chrome, Firefox o Edge
2. En la barra de direcciones, escribe: `http://127.0.0.1:8000/`
3. Presiona Enter

**¡BOOM! 💥** Verás tu página de inicio hermosa con colores morados.

### 3.2 Explorar las páginas

Haz clic en los botones del menú de arriba:

- **Inicio** - La página principal
- **Calificaciones** - Ver todas las calificaciones (aún no hay ninguna)
- **Nueva Calificación** - Crear una calificación
- **Promedio General** - Ver el promedio de todos

## ✏️ Paso 4: Crear tu primera calificación

### 4.1 Iniciar sesión

1. Haz clic en **"Iniciar Sesión"** (arriba a la derecha)
2. Escribe el usuario y contraseña que creaste antes
3. Haz clic en **"Iniciar Sesión"**

**Nota**: Por ahora, como Helen no ha hecho su parte, esta página no existe todavía. Así que vamos a usar el admin de Django.

### 4.2 Ir al admin de Django

1. En el navegador, escribe: `http://127.0.0.1:8000/admin/`
2. Inicia sesión con tu usuario y contraseña
3. Verás el panel de administración

### 4.3 Crear una calificación desde el admin

1. Haz clic en **"Calificaciones"**
2. Haz clic en **"Agregar Calificación"** (botón verde arriba a la derecha)
3. Llena el formulario:
   - **Nombre del estudiante**: María García
   - **Identificación**: 12345678
   - **Asignatura**: Matemáticas
   - **Nota 1**: 85
   - **Nota 2**: 90
   - **Nota 3**: 88
4. Haz clic en **"Guardar"**

**¡Mira!** El promedio se calculó automáticamente: (85 + 90 + 88) / 3 = 87.67

### 4.4 Crear más calificaciones

Crea al menos 3 calificaciones más para que puedas ver cómo funciona todo.

Ejemplos:
- Juan Pérez - Español - 75, 80, 78
- Ana López - Ciencias - 92, 95, 90
- Carlos Ruiz - Historia - 70, 75, 72

## 👀 Paso 5: Ver tus calificaciones

### 5.1 Ir a la lista de calificaciones

1. En el navegador, escribe: `http://127.0.0.1:8000/calificaciones/`
2. Verás una tabla hermosa con todas las calificaciones

**¿Qué ves?**
- Una tabla con todas las calificaciones
- Los nombres de los estudiantes
- Las tres notas de cada uno
- El promedio calculado automáticamente
- Botones para editar (amarillo) y eliminar (rojo)
- Arriba, dos tarjetas moradas con:
  - Total de registros
  - Promedio general de todos

## ✨ Paso 6: Editar una calificación

### 6.1 Hacer clic en el botón de editar

1. En la lista de calificaciones, busca una calificación
2. Haz clic en el botón amarillo con el lápiz (editar)
3. Verás el formulario con los datos actuales

### 6.2 Cambiar las notas

1. Cambia alguna nota (por ejemplo, cambia 85 por 95)
2. Haz clic en **"Actualizar Calificación"**
3. Verás un mensaje verde: "¡Calificación actualizada exitosamente!"
4. El promedio se recalculó automáticamente

## 🗑️ Paso 7: Eliminar una calificación

### 7.1 Hacer clic en el botón de eliminar

1. En la lista de calificaciones, busca una calificación
2. Haz clic en el botón rojo con la basura (eliminar)
3. Verás una página de confirmación

### 7.2 Confirmar la eliminación

1. Lee la información de la calificación que vas a eliminar
2. Si estás segura, haz clic en **"Sí, Eliminar Calificación"**
3. Si te arrepentiste, haz clic en **"No, Cancelar"**

## 🧮 Paso 8: Ver el promedio general

### 8.1 Ir a la página de promedio general

1. Haz clic en **"Promedio General"** en el menú
2. O escribe: `http://127.0.0.1:8000/promedio-general/`

**¿Qué ves?**
- Un número grande en el centro (el promedio de todos)
- Tres tarjetas con estadísticas:
  - Total de estudiantes
  - Promedio general
  - Calificación (A, B o C)
- Explicación de cómo se calculó

## 📱 Paso 9: Probar en el celular

### 9.1 Encontrar tu IP

1. En la terminal, escribe: `ipconfig`
2. Busca "Dirección IPv4" (algo como: 192.168.1.100)

### 9.2 Abrir en el celular

1. Asegúrate de que tu celular esté en la misma red WiFi
2. En el celular, abre el navegador
3. Escribe: `http://TU_IP:8000/` (ejemplo: http://192.168.1.100:8000/)

**¡Funciona en el celular también!** 📱

## 🎨 Paso 10: Entender el diseño

### ¿Por qué se ve tan bonito?

1. **Bootstrap 5** - Es como una caja de herramientas con botones, tablas y formularios bonitos
2. **Font Awesome** - Son los iconitos que ves (⭐, 📝, 🗑️, etc.)
3. **Google Fonts** - La letra bonita (Poppins)
4. **CSS personalizado** - Los colores morados y las animaciones

### Los colores

- **Morado** (#667eea → #764ba2) - Color principal
- **Verde** (#10b981) - Para éxito y crear
- **Amarillo** (#f59e0b) - Para editar
- **Rojo** (#ef4444) - Para eliminar
- **Azul** (#3b82f6) - Para información

## 🔧 Paso 11: ¿Cómo funciona por dentro?

### El flujo de una calificación

```
1. Usuario llena el formulario
   ↓
2. Django recibe los datos
   ↓
3. El modelo calcula el promedio automáticamente
   ↓
4. Se guarda en la base de datos
   ↓
5. Django muestra un mensaje de éxito
   ↓
6. Redirige a la lista de calificaciones
```

### El código mágico del promedio

```python
def calcular_promedio(self):
    # Suma las tres notas y divide entre 3
    return round((self.nota1 + self.nota2 + self.nota3) / 3, 2)

def save(self, *args, **kwargs):
    # Antes de guardar, calcula el promedio
    self.promedio = self.calcular_promedio()
    # Ahora sí guarda
    super().save(*args, **kwargs)
```

**¿Qué hace esto?**
- Cada vez que guardas una calificación
- Automáticamente suma las tres notas
- Las divide entre 3
- Redondea a 2 decimales
- Y guarda ese número en el campo "promedio"

## 🎯 Paso 12: Preparar para Helen

### ¿Qué falta?

Helen va a hacer la parte de **autenticación**:

1. **Login** - Para que los usuarios puedan entrar
2. **Logout** - Para que puedan salir
3. **Registro** - Para que nuevos usuarios se registren
4. **Recuperar contraseña** - Por si olvidan su contraseña

### ¿Cómo van a trabajar juntas?

```
TÚ (Jiliana)                    HELEN
    |                              |
    |-- Subes tu código a GitHub   |
    |                              |
    |                              |-- Descarga tu código
    |                              |
    |                              |-- Crea su rama
    |                              |
    |                              |-- Hace su parte
    |                              |
    |                              |-- Sube su código
    |                              |
    |-- Revisas su código          |
    |                              |
    |-- Apruebas y haces merge     |
    |                              |
    |-- ¡Proyecto completo! 🎉     |
```

## 📝 Paso 13: Subir a GitHub

### 13.1 Crear cuenta en GitHub (si no tienes)

1. Ve a https://github.com
2. Haz clic en "Sign up"
3. Crea tu cuenta

### 13.2 Crear un repositorio

1. Haz clic en el botón verde "New" (arriba a la derecha)
2. Nombre: `sistema-calificaciones-django`
3. Descripción: `Sistema de gestión de calificaciones - Laboratorio Final`
4. Selecciona "Public" o "Private"
5. **NO** marques ninguna casilla
6. Haz clic en "Create repository"

### 13.3 Subir tu código

En la terminal (donde tienes tu proyecto):

```bash
# 1. Inicializar Git
git init

# 2. Agregar todos los archivos
git add .

# 3. Hacer el primer commit
git commit -m "feat: implementación completa del CRUD de calificaciones"

# 4. Conectar con GitHub (reemplaza <TU_USUARIO> con tu usuario)
git remote add origin https://github.com/<TU_USUARIO>/sistema-calificaciones-django.git

# 5. Subir a GitHub
git push -u origin main
```

**¡Listo!** Tu código ya está en GitHub.

## 🎉 Paso 14: ¡Felicidades!

### ¿Qué has logrado?

✅ Creaste un sistema web completo
✅ Con diseño profesional y bonito
✅ Que funciona perfectamente
✅ Con CRUD completo
✅ Con cálculos automáticos
✅ Responsive (funciona en celular)
✅ Listo para trabajo en equipo

### Puntuación del laboratorio

| Criterio | Puntos | Estado |
|----------|--------|--------|
| Estructura del proyecto | 0.5 | ✅ |
| Modelo y cálculo | 1.0 | ✅ |
| Vistas CRUD | 1.0 | ✅ |
| Promedio general | 1.0 | ✅ |
| Plantillas y diseño | 1.5 | ✅ |
| **TOTAL** | **5.0** | **✅** |

## 🆘 Si algo sale mal

### Error: "No module named django"

```bash
pip install django
```

### Error: "Port already in use"

```bash
# Detén el servidor con Ctrl+C
# Luego vuelve a ejecutar:
python manage.py runserver
```

### Error: "Table doesn't exist"

```bash
python manage.py migrate
```

### La página se ve fea (sin colores)

1. Verifica que tengas internet (Bootstrap y Font Awesome se cargan de internet)
2. Refresca la página con Ctrl+F5

## 📚 Recursos para aprender más

- **Django Docs**: https://docs.djangoproject.com/
- **Bootstrap**: https://getbootstrap.com/
- **W3Schools**: https://www.w3schools.com/
- **YouTube**: Busca "Django tutorial español"

## 💡 Consejos finales

1. **No tengas miedo de experimentar** - Si algo se rompe, puedes arreglarlo
2. **Lee los mensajes de error** - Te dicen qué está mal
3. **Usa Google** - Todos los programadores lo hacen
4. **Pide ayuda** - A tus compañeros, profesores o en foros
5. **Practica** - Mientras más practiques, mejor serás

## 🌟 Próximos pasos

1. **Espera a que Helen termine su parte**
2. **Prueben todo junto**
3. **Desplieguen en Vercel** (para que esté en internet)
4. **Presenten su proyecto**
5. **¡Obtengan su 5.0! 🎉**

---

**¡Eres increíble! Has creado algo asombroso. 💜✨**

**Recuerda**: Todos los programadores empezaron sin saber nada. Lo importante es seguir aprendiendo y practicando.

**¡Mucho éxito en tu proyecto! 🚀**
