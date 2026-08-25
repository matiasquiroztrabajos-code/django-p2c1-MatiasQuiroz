from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }

    return render(
        request,
        "dispositivos/inicio.html",
        contexto
    )


def dispositivos_zona(request, zona_id):
    if zona_id != 3:
        return HttpResponse(
            "Zona no encontrada", status=404
        )

    return HttpResponse(
        f"Dispositivos de la zona {zona_id}"
    )


def dispositivos_game(request, game_id):
    if game_id != 5:
        return HttpResponse(
            "No existe juego lo siento perdon", status=404
        )

    return HttpResponse(
        f"Jueguito numero {game_id}"
    )


def catalogo(request):
    dispositivos = [
        {"nombre": "Medidor inteligente", "estado": "Activo"},
        {"nombre": "Sensor de temperatura", "estado": "Activo"},
        {"nombre": "Climatizador", "estado": "Revisión"},
    ]

    return render(
        request,
        "dispositivos/catalogo.html",
        {"dispositivos": dispositivos},
    )
