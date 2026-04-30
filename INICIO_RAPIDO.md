# ⚡ INICIO RÁPIDO - 5 Minutos

## 🎯 Para empezar AHORA MISMO

### 1️⃣ Crear superusuario (30 segundos)

```bash
python manage.py createsuperuser
```

- Usuario: `admin`
- Email: (presiona Enter)
- Contraseña: `admin123` (o la que quieras)

### 2️⃣ Iniciar servidor (10 segundos)

```bash
python manage.py runserver
```

### 3️⃣ Abrir navegador (5 segundos)

Ve a: **http://127.0.0.1:8000/**

### 4️⃣ Crear calificaciones (2 minutos)

1. Ve a: **http://127.0.0.1:8000/admin/**
2. Login con tu usuario
3. Haz clic en "Calificaciones" → "Agregar"
4. Llena el formulario y guarda
5. Crea 3-4 calificaciones más

### 5️⃣ Ver tu trabajo (1 minuto)

Ve a: **http://127.0.0.1:8000/calificaciones/**

**¡LISTO! Ya tienes tu sistema funcionando. 🎉**

---

## 📚 Documentación Completa

- **README.md** - Documentación completa del proyecto
- **TUTORIAL_PASO_A_PASO.md** - Tutorial detallado para principiantes
- **COMANDOS_JILIANA.md** - Todos los comandos que necesitas
- **INSTRUCCIONES_HELEN.md** - Guía para Helen
- **RESUMEN_PROYECTO.md** - Resumen técnico del proyecto

---

## 🚀 Subir a GitHub (3 minutos)

```bash
git init
git add .
git commit -m "feat: proyecto completo"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/sistema-calificaciones-django.git
git push -u origin main
```

---

## 🎨 URLs Importantes

| URL | Descripción |
|-----|-------------|
| http://127.0.0.1:8000/ | Inicio |
| http://127.0.0.1:8000/admin/ | Admin Django |
| http://127.0.0.1:8000/calificaciones/ | Lista |
| http://127.0.0.1:8000/calificaciones/crear/ | Crear |
| http://127.0.0.1:8000/promedio-general/ | Promedio |

---

## ✅ Checklist Rápido

- [ ] Servidor corriendo
- [ ] Superusuario creado
- [ ] Al menos 3 calificaciones creadas
- [ ] Probaste crear, editar y eliminar
- [ ] Viste el promedio general
- [ ] Subiste a GitHub

---

## 🆘 Problemas Comunes

**Error: "No module named django"**
```bash
pip install django
```

**Error: "Port already in use"**
```bash
# Presiona Ctrl+C y vuelve a ejecutar
python manage.py runserver
```

**Error: "Table doesn't exist"**
```bash
python manage.py migrate
```

---

## 📞 Ayuda

Si necesitas ayuda detallada, lee:
1. **TUTORIAL_PASO_A_PASO.md** (para principiantes)
2. **README.md** (documentación completa)
3. **COMANDOS_JILIANA.md** (todos los comandos)

---

**¡Éxito! 🚀💜**
