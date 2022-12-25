from pathlib import Path
from django.urls import path

from wordChampion_api import views

urlpatterns = [
    path('test-protegido/', views.puntoProtegido),

    path('equipo/<int:id>', views.mostrarJugadores),
    path('jugador/editar/<int:id>', views.gestionarJugador)
]