Django P2C1 - Matías Quiroz

Proyecto desarrollado en Python y Django como parte de la práctica de backend.

📋 Descripción

Este proyecto consiste en una aplicación web desarrollada con Django, utilizando la estructura estándar de un proyecto Django y una aplicación denominada dispositivos.

El objetivo es poner en práctica conceptos fundamentales del desarrollo backend con Python y Django, incluyendo la organización de proyectos, aplicaciones, templates, URLs, vistas y modelos.

🛠️ Tecnologías utilizadas
Python
Django 6.1
HTML / Templates de Django
SQLite (base de datos por defecto de Django)
Git / GitHub
📁 Estructura del proyecto
django-p2c1-MatiasQuiroz/
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── dispositivos/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│
├── .gitignore
├── archivo.txt
├── manage.py
└── requirements.txt

🚀 Instalación
1. Clonar el repositorio
git clone https://github.com/matiasquiroztrabajos-code/django-p2c1-MatiasQuiroz.git

2. Ingresar al proyecto
cd django-p2c1-MatiasQuiroz

3. Crear un entorno virtual

En Windows:

python -m venv venv
venv\Scripts\activate


En Linux / macOS:

python3 -m venv venv
source venv/bin/activate

4. Instalar las dependencias
pip install -r requirements.txt

▶️ Ejecutar el proyecto

Antes de iniciar el servidor, ejecutar las migraciones:

python manage.py migrate


Luego iniciar el servidor de desarrollo:

python manage.py runserver


El proyecto estará disponible en:

http://127.0.0.1:8000/

🧩 Aplicación dispositivos

La aplicación principal del proyecto se encuentra en la carpeta dispositivos.

Dentro de ella se encuentran los archivos principales de una aplicación Django:

models.py: definición de los modelos y estructura de datos.
views.py: lógica encargada de procesar las solicitudes.
urls.py: rutas asociadas a la aplicación.
admin.py: configuración para el panel de administración de Django.
tests.py: espacio destinado a las pruebas.
migrations/: archivos relacionados con las migraciones de la base de datos.
📦 Dependencias

Las principales dependencias utilizadas se encuentran especificadas en requirements.txt:

Django==6.1
asgiref==3.12.1
sqlparse==0.6.0
tzdata==2026.3

🎯 Objetivo

El proyecto fue realizado con fines educativos para practicar el desarrollo backend utilizando Django y comprender la estructura básica de una aplicación web basada en Python.

👨‍💻 Autor

Matías Quiroz
