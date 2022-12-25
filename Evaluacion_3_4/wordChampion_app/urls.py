from django.urls import path

from wordChampion_app import views


urlpatterns = [
    path('equipo/<int:id>', views.mostrarEquipo),
    path('equipo', views.mostrarEquipos)
]