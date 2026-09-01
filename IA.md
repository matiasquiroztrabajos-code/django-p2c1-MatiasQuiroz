# Uso de Inteligencia Artificial — Fase 1 EcoEnergy

## Herramienta utilizada

Claude (Anthropic), a través de una conversación asistida en el chat de
Claude, con acceso a un entorno de ejecución (bash/Python) para instalar
dependencias y correr `python manage.py check` y `python manage.py
runserver` sobre el proyecto real.

## Qué se le pidió a la IA

1. Que revisara el estado del repositorio (Clases 2 a 4 ya implementadas)
   antes de construir nada nuevo.
2. Que propusiera la estructura de los tres archivos JSON (`zonas.json`,
   `categorias.json`, `dispositivos.json`) con datos de ejemplo coherentes,
   respetando las claves y mínimos exigidos por el enunciado.
3. Que implementara `dispositivos/services.py` con funciones de carga de
   JSON, siguiendo el mismo patrón mostrado en la Clase 5
   (`cargar_dispositivos` con `json.load` y `settings.BASE_DIR`).
4. Que implementara las Views `listado_zonas` y `detalle_zona` en
   `dispositivos/views.py`, calculando cantidad de dispositivos, consumo
   total y estado (NORMAL/ALERTA) en Python.
5. Que propusiera una estructura HTML/Bootstrap para `base.html`,
   `zonas.html` y `zona_detalle.html`, con un estilo "un poco más
   elaborado" (colores propios de EcoEnergy e íconos de Bootstrap Icons),
   ya que expresamente se decidió no seguir el boceto de forma literal.
6. Que instalara y registrara `django-bootstrap5` como dependencia externa.

## Prompts relevantes

- "Lee estos apuntes de la Unidad 1, solo debo codificar en base a esto."
- "Elimina las views/urls de labs anteriores que ya no correspondan
  (catalogo, dispositivos_zona, dispositivos_game) y deja solo inicio +
  las rutas nuevas de EcoEnergy."
- "Invéntame datos de zonas, categorías y dispositivos coherentes y
  suficientes para EcoEnergy."
- "Quiero un diseño Bootstrap un poco más elaborado, con colores propios
  de EcoEnergy e íconos."

## Qué se usó tal cual y qué se adaptó

- Se usó tal cual la estructura de `services.py` (carga de JSON) por ser
  exactamente el patrón enseñado en la Clase 5.
- Se adaptaron los nombres de zonas/dispositivos/categorías y los valores
  de `consumo_kwh` para asegurar que existiera al menos un caso NORMAL y
  un caso ALERTA, y una zona sin dispositivos, cubriendo los escenarios de
  prueba exigidos en la Sección 6 del enunciado.
- Se revisó y se comprende cada línea de `views.py`: por qué se usa
  `next(... , None)` para buscar la zona/categoría, por qué se devuelve
  `HttpResponse(status=404)` en lugar de dejar que Django lance un error
  no controlado, y por qué el cálculo de `consumo_total` y `estado` vive en
  la View y no en el Template.
- El diseño Bootstrap (colores, tarjetas, badges, íconos) fue una
  propuesta de la IA que se aceptó y se dejó tal cual, dado que el
  enunciado indica explícitamente que el boceto es referencial y no exige
  reproducir colores ni distribución exacta.

## Verificación y pruebas realizadas

Se corrieron directamente durante el desarrollo (evidencia registrada en
la conversación con la IA):

- `python manage.py check` → sin errores.
- `GET /` → 200.
- `GET /zonas/` → 200, muestra las 4 zonas.
- `GET /zonas/1/` → 200, estado NORMAL (115/150 kWh).
- `GET /zonas/2/` → 200, estado ALERTA (850/800 kWh).
- `GET /zonas/4/` → 200, mensaje "Esta zona no tiene dispositivos".
- `GET /zonas/99/` → 404.

## Declaración

El estudiante comprende y puede explicar cada parte del código entregado.
La IA se usó como apoyo para acelerar la redacción y para proponer y
verificar el diseño Bootstrap, no para generar una solución que no pueda
ser explicada.
