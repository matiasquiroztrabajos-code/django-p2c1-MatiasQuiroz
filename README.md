# EcoEnergy — Fase 1 (Programación Back End · TI3041)

Aplicación Django del lado del servidor para consultar zonas de consumo
energético y los dispositivos instalados en cada una. Esta primera versión
utiliza archivos JSON como fuente de datos.

## Tecnologías utilizadas

- Python
- Django 6.1
- django-bootstrap5 (Bootstrap 5 integrado a los Templates)
- HTML / Templates de Django (herencia con `base.html`)
- Archivos JSON como fuente de datos (`data/`)
- Git / GitHub

## Requisitos previos

- Python 3.11 o superior instalado.
- Git instalado.

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/matiasquiroztrabajos-code/django-p2c1-MatiasQuiroz.git
   cd django-p2c1-MatiasQuiroz
   ```

2. Crear el entorno virtual:

   En Git Bash / Linux / macOS:

   ```bash
   python -m venv .venv
   source .venv/Scripts/activate   # Git Bash en Windows
   # source .venv/bin/activate     # Linux / macOS
   ```

   En PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Instalar las dependencias:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Ejecución

```bash
python manage.py check
python manage.py runserver
```

El proyecto estará disponible en `http://127.0.0.1:8000/`.

## Rutas funcionales

| Ruta                         | Descripción                                              |
|-------------------------------|-----------------------------------------------------------|
| `/`                            | Página de inicio de EcoEnergy.                             |
| `/zonas/`                      | Listado de zonas registradas en `data/zonas.json`.         |
| `/zonas/<id>/`                 | Detalle de una zona: dispositivos, categoría, consumo total y estado (NORMAL/ALERTA). Responde `404` si el `id` no existe. |

## Fuente de datos

La aplicación carga tres archivos JSON ubicados en `data/`:

- `data/zonas.json`: zonas de consumo (`id`, `nombre`, `limite_kwh`).
- `data/categorias.json`: categorías de dispositivo (`id`, `nombre`,
  `descripcion`).
- `data/dispositivos.json`: dispositivos (`id`, `nombre`, `consumo_kwh`,
  `zona_id`, `categoria_id`).

La función `dispositivos/services.py` carga cada archivo con `json.load`, y
las Views (`dispositivos/views.py`) resuelven las relaciones entre archivos
mediante los identificadores (`zona_id`, `categoria_id`), calculan el
consumo total por zona y determinan el estado `NORMAL` o `ALERTA`
comparando `consumo_total` contra `limite_kwh`.

## Pruebas realizadas

- `python manage.py check` → sin errores.
- `GET /zonas/` → lista las 4 zonas registradas.
- `GET /zonas/1/` → zona con consumo bajo el límite → estado `NORMAL`.
- `GET /zonas/2/` → zona con consumo sobre el límite → estado `ALERTA`.
- `GET /zonas/4/` → zona sin dispositivos → mensaje "Esta zona no tiene
  dispositivos".
- `GET /zonas/99/` → identificador inexistente → `404`.

## Estado actual y próximos pasos

- Completado: entorno, proyecto Django, app `dispositivos`, Templates con
  herencia y Bootstrap, carga de datos desde JSON, listado y detalle de
  zonas con cálculo dinámico de consumo y estado.
- Fuera de alcance en esta fase (según enunciado): Models, migraciones,
  ORM, CRUD, formularios, autenticación, permisos y soft delete.
- Próximo paso (Fase 2, cuando se publique): a definir según el
  instrumento completo de la Evaluación Sumativa I.

## Aplicación `dispositivos`

La aplicación principal del proyecto se encuentra en la carpeta
`dispositivos`. Dentro de ella:

- `views.py`: lógica encargada de procesar las solicitudes (inicio,
  listado de zonas, detalle de zona).
- `services.py`: funciones de carga de los archivos JSON.
- `urls.py`: rutas asociadas a la aplicación.
- `admin.py`, `models.py`, `migrations/`: presentes por defecto de
  `startapp`, sin uso en esta fase (no se solicitan Models ni ORM).
- `tests.py`: espacio destinado a pruebas.

## Dependencias

Las dependencias del proyecto están especificadas en `requirements.txt`:

```
asgiref==3.12.1
Django==6.1
django-bootstrap5==26.3
sqlparse==0.6.0
tzdata==2026.3
```

`django-bootstrap5` se utiliza para cargar los estilos y scripts de
Bootstrap 5 desde los Templates (`{% bootstrap_css %}` y
`{% bootstrap_javascript %}` en `base.html`), evitando escribir el HTML de
integración manualmente en cada página.
