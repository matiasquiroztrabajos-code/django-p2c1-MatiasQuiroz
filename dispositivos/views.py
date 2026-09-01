from django.http import HttpResponse
from django.shortcuts import render

from .services import cargar_categorias, cargar_dispositivos, cargar_zonas


def inicio(request):
    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }

    return render(request, "dispositivos/inicio.html", contexto)


def listado_zonas(request):
    zonas = cargar_zonas()
    dispositivos = cargar_dispositivos()

    zonas_con_resumen = []
    for zona in zonas:
        cantidad_dispositivos = sum(
            1 for dispositivo in dispositivos
            if dispositivo["zona_id"] == zona["id"]
        )
        zonas_con_resumen.append({
            "id": zona["id"],
            "nombre": zona["nombre"],
            "limite_kwh": zona["limite_kwh"],
            "cantidad_dispositivos": cantidad_dispositivos,
        })

    contexto = {"zonas": zonas_con_resumen}

    return render(request, "dispositivos/zonas.html", contexto)


def detalle_zona(request, zona_id):
    zonas = cargar_zonas()
    zona = next((z for z in zonas if z["id"] == zona_id), None)

    if zona is None:
        return HttpResponse("Zona no encontrada", status=404)

    categorias = cargar_categorias()
    dispositivos = cargar_dispositivos()

    dispositivos_zona = []
    consumo_total = 0
    for dispositivo in dispositivos:
        if dispositivo["zona_id"] != zona["id"]:
            continue

        categoria = next(
            (c for c in categorias if c["id"] == dispositivo["categoria_id"]),
            None,
        )
        nombre_categoria = categoria["nombre"] if categoria else "Sin categoría"

        dispositivos_zona.append({
            "nombre": dispositivo["nombre"],
            "categoria": nombre_categoria,
            "consumo_kwh": dispositivo["consumo_kwh"],
        })
        consumo_total += dispositivo["consumo_kwh"]

    estado = "ALERTA" if consumo_total > zona["limite_kwh"] else "NORMAL"

    contexto = {
        "zona": zona,
        "dispositivos": dispositivos_zona,
        "consumo_total": consumo_total,
        "estado": estado,
    }

    return render(request, "dispositivos/zona_detalle.html", contexto)
