# Análisis de datos — EcoEnergy (Fase 1)

## 1. Relaciones y multiplicidades

Modelo entregado en el enunciado (Figura 1):

- **Zona 1 — 0..\* Dispositivo**: una zona contiene cero o muchos dispositivos;
  cada dispositivo pertenece exactamente a una zona.
- **Categoria 1 — 0..\* Dispositivo**: una categoría clasifica cero o muchos
  dispositivos; cada dispositivo pertenece exactamente a una categoría.

No existen Models ni ORM en esta fase (fuera de alcance). Las relaciones se
implementan mediante identificadores dentro de los archivos JSON, y se
resuelven en Python al momento de procesar la solicitud.

## 2. Claves de conexión

| Archivo             | Clave primaria | Claves foráneas (referencian a)      |
|----------------------|----------------|----------------------------------------|
| `data/zonas.json`       | `id`           | —                                        |
| `data/categorias.json`  | `id`           | —                                        |
| `data/dispositivos.json`| `id`           | `zona_id` → `zonas.id`, `categoria_id` → `categorias.id` |

Cada `zona_id` y `categoria_id` presente en `dispositivos.json` corresponde a
un `id` existente en `zonas.json` y `categorias.json` respectivamente. Los
`id` son únicos dentro de cada archivo.

## 3. Cómo se resuelven las relaciones en el código

1. `dispositivos/services.py` carga cada archivo JSON de forma independiente
   (`cargar_zonas`, `cargar_categorias`, `cargar_dispositivos`), devolviendo
   listas de diccionarios de Python.
2. `listado_zonas` (View) recorre `zonas` y, para cada una, cuenta cuántos
   elementos de `dispositivos` tienen `zona_id` igual al `id` de la zona.
   Ese conteo viaja al Template mediante el contexto; el Template no filtra
   ni calcula nada.
3. `detalle_zona` (View) busca la zona solicitada por `id`. Si no existe,
   responde `HttpResponse(..., status=404)` sin tocar el Template. Si existe,
   filtra los dispositivos cuyo `zona_id` coincide, y por cada uno busca su
   categoría por `categoria_id` para obtener el nombre legible. Además
   acumula `consumo_total` y calcula `estado` (`ALERTA` si
   `consumo_total > limite_kwh`, `NORMAL` en caso contrario).
4. El Template solo recibe y presenta los datos ya resueltos (nombre de
   zona, límite, consumo total, estado, y la lista de dispositivos con su
   categoría). No contiene lógica de negocio.

Como la relación se resuelve dinámicamente sobre las listas cargadas en cada
solicitud, agregar registros válidos a los JSON (nuevas zonas, categorías o
dispositivos) se refleja automáticamente sin modificar Views ni Templates.

## 4. Matriz Criterio de aceptación | Archivo/Componente | Prueba

| Criterio | Archivo / Componente                                  | Prueba realizada |
|----------|--------------------------------------------------------|-------------------|
| CA-01    | `dispositivos/views.py` (`listado_zonas`), `zonas.html` | `GET /zonas/` muestra las 4 zonas de `zonas.json`. |
| CA-02    | `zonas.html`                                            | Cada tarjeta muestra nombre, límite y cantidad de dispositivos, con enlace a "Ver detalle". |
| CA-03    | `views.py` (`detalle_zona`), `zona_detalle.html`        | `GET /zonas/1/` muestra dispositivos, categoría, consumo y métricas. |
| CA-04    | `views.py` (`detalle_zona`, `listado_zonas`)             | `total`, `consumo_total`, `cantidad_dispositivos` y `estado` se calculan en Python, no están escritos en el HTML. |
| CA-05    | `views.py` (`detalle_zona`)                              | Zona 1 (115/150 kWh) responde NORMAL; Zona 2 (850/800 kWh) responde ALERTA. |
| CA-06    | `dispositivos/services.py`                               | Se agregaron dos dispositivos de prueba al JSON y aparecieron en el listado y el detalle sin tocar código. |
| CA-07    | `views.py` (`detalle_zona`), `zona_detalle.html`         | Zona 4 (`Sala de Servidores`) no tiene dispositivos y muestra el mensaje "Esta zona no tiene dispositivos". |
| CA-08    | `views.py` (`detalle_zona`)                              | `GET /zonas/99/` responde `404` con `HttpResponse`. |
| CA-09    | `base.html`, `zonas.html`, `zona_detalle.html`           | Se probó duplicando registros del JSON; la navegación y estructura se mantuvieron. |
| CA-10    | `zona_detalle.html` (`.table-responsive-eco`)             | La tabla usa `table-responsive` con `max-height` y scroll vertical/horizontal propio de Bootstrap. |
| CA-11    | `base.html` y templates hijos                             | Header, nav, tarjetas, tabla y botones siguen la jerarquía visual de Bootstrap con la paleta EcoEnergy. |
| CA-12    | `zona_detalle.html`                                       | El estado se comunica con texto ("NORMAL"/"ALERTA") + ícono + color de badge, no solo color. |
| CA-13    | Proyecto completo                                          | `python manage.py check` → "System check identified no issues". |
