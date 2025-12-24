# 🚀 TecnoKev Portfolio

Portafolio personal desarrollado con Django, presentando mis proyectos, blog técnico y cursos. Diseño moderno con tema oscuro y efectos visuales avanzados.

![Django](https://img.shields.io/badge/Django-5.2-green?style=flat&logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-purple?style=flat&logo=bootstrap)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

## ✨ Características

- 🎨 **Diseño Moderno**: Interfaz oscura con efectos de paralaje y animaciones fluidas
- 📱 **Responsive**: Adaptable a cualquier dispositivo (móvil, tablet, desktop)
- 📝 **Sistema de Blog**: Publicación de artículos con categorías, editor rico (CKEditor) y URLs amigables (slugs)
- 💬 **Comentarios**: Sistema de comentarios integrado con Giscus (GitHub Discussions)
- 🎯 **Proyectos Interactivos**: Galería de proyectos con filtros por categoría y carrusel Swiper
- 📊 **Contador de Visitas**: Tracking discreto con animación lazy-load
- 🔗 **Redes Sociales**: Enlaces directos a YouTube, TikTok, Instagram, Facebook, LinkedIn, GitHub
- 🔍 **SEO Optimizado**: URLs semánticas y meta tags optimizados

## 🛠️ Tecnologías

### Backend
- **Django 5.2.6**: Framework web principal
- **Python 3.11**: Lenguaje de programación
- **SQLite**: Base de datos
- **CKEditor**: Editor WYSIWYG para contenido rico

### Frontend
- **Bootstrap 5.3.3**: Framework CSS con tema oscuro
- **Font Awesome 6.5.2**: Iconografía
- **Swiper.js 11**: Carruseles y sliders interactivos
- **Vanilla Tilt.js 1.7.2**: Efectos 3D en tarjetas
- **CSS3**: Animaciones y estilos personalizados
- **JavaScript**: Interactividad y efectos

### Integraciones
- **Giscus**: Sistema de comentarios basado en GitHub Discussions
- **Contador de Visitas**: Analytics integrado

## 📁 Estructura del Proyecto

```
portafolio/
├── apps/
│   ├── blog/              # Sistema de blog
│   │   ├── models.py      # Modelos Blog, Comentario
│   │   ├── views.py       # Vistas de listado y detalle
│   │   ├── urls.py        # URLs con slugs
│   │   └── templates/     # Plantillas de blog
│   ├── configuraciones/   # Modelos compartidos (Categoría)
│   ├── curso/             # Gestión de cursos
│   ├── index/             # Página principal
│   └── proyecto/          # Portafolio de proyectos
├── media/                 # Archivos subidos
├── static/
│   ├── css/              # Estilos personalizados
│   │   └── modern-styles.css
│   ├── img/              # Imágenes estáticas
│   └── js/               # Scripts personalizados
│       ├── main.js       # Funcionalidad principal
│       └── swiper.js     # Configuración de carruseles
├── templates/
│   └── base/
│       └── base_portafolio.html  # Template base
├── portafolio/           # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3            # Base de datos
├── manage.py
└── requirements.txt      # Dependencias
```

## 🚀 Instalación

### Prerrequisitos
- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/portafolio-tecnokev.git
cd portafolio-tecnokev
```

2. **Crear entorno virtual**
```bash
python -m venv .venv
```

3. **Activar entorno virtual**

Windows:
```bash
.venv\Scripts\activate
```

Linux/Mac:
```bash
source .venv/bin/activate
```

4. **Instalar dependencias**
```bash
cd portafolio
pip install -r requirements.txt
```

5. **Realizar migraciones**
```bash
python manage.py migrate
```

6. **Crear superusuario**
```bash
python manage.py createsuperuser
```

7. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

8. **Acceder a la aplicación**
- Frontend: http://localhost:8000
- Admin: http://localhost:8000/admin

## ⚙️ Configuración

### Configuraciones Locales

Crea un archivo `configuraciones_locales.py` en `portafolio/portafolio/` para configuraciones personales:

```python
# Configuraciones de desarrollo
DEBUG = True
SECRET_KEY = 'tu-clave-secreta-aqui'

# Base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Archivos estáticos y media
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Giscus (Comentarios)

1. Habilita GitHub Discussions en tu repositorio
2. Instala la app Giscus en tu cuenta de GitHub
3. Obtén tu configuración en [giscus.app](https://giscus.app/)
4. Actualiza los datos en `blog_detalle.html`

## 📝 Uso

### Panel de Administración

1. Accede a `/admin`
2. Gestiona:
   - **Blogs**: Crea artículos con título, contenido rico, categorías e imágenes
   - **Proyectos**: Añade proyectos con descripción y capturas
   - **Cursos**: Publica tus formaciones y talleres
   - **Categorías**: Organiza el contenido
   - **Comentarios**: Modera comentarios de blogs

### Creación de Contenido

**Nuevo Blog:**
1. Panel Admin → Blog → Agregar
2. Completa título (el slug se genera automáticamente)
3. Añade descripción y contenido con el editor CKEditor
4. Sube imagen destacada
5. Asigna categorías
6. Marca como vigente para publicar

**Nuevo Proyecto:**
1. Panel Admin → Proyecto → Agregar
2. Completa información del proyecto
3. Sube imágenes/capturas
4. Asigna categorías para filtros

## 🎨 Personalización

### Estilos
- Modifica `static/css/modern-styles.css` para cambiar colores, tipografía y efectos
- Variables CSS para tema oscuro están en la sección `:root`

### Scripts
- `static/js/main.js`: Animaciones, reveal on scroll, contador de visitas
- `static/js/swiper.js`: Configuración de carruseles y filtros

### Plantillas
- `templates/base/base_portafolio.html`: Estructura base, navbar, footer
- Cada app tiene su carpeta `templates/` con vistas específicas

## 🔐 Seguridad

- ⚠️ Nunca subas `configuraciones_locales.py` a GitHub
- Cambia `SECRET_KEY` en producción
- Configura `DEBUG = False` en producción
- Usa variables de entorno para datos sensibles
- Configura HTTPS en el servidor de producción

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

## 👤 Contacto

**Kevin Aguero** - TecnoKev

- 🌐 Website: [tu-sitio.com]
- 📧 Email: [tu-email@ejemplo.com]
- 💼 LinkedIn: [linkedin.com/in/tu-perfil](https://www.linkedin.com/in/kevinaguero1/)
- 🐙 GitHub: [@tu-usuario](https://github.com/tu-usuario)
- 📺 YouTube: [youtube.com/@tecnokev](https://www.youtube.com/@tecnokev)
- 📸 Instagram: [@tecnokev](https://www.instagram.com/tecnokev/)

---

⭐ Si este proyecto te resulta útil, ¡no olvides darle una estrella!
