from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from wordChampion_api.models import Equipo, Jugador
from .serializers import EquipoSerializer, JugadorSerializer


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def puntoProtegido(request):
    return Response ({'status':'OK'}, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
@permission_classes((AllowAny,))
def mostrarJugadores(request, id):
    try:
        jugadores = Jugador.objects.get(equipo=id)
        serializado = JugadorSerializer(jugadores)
        return Response(serializado.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['PATCH', 'DELETE', 'POST'])
@permission_classes((IsAuthenticated,))
def gestionarJugador(request, id):
    if request.method == 'PATCH':
        try:
            jugador = Jugador.objects.get(id=id)
            serializador = JugadorSerializer(jugador, data=request.data, partial=True)
            if serializador.is_valid():
                serializador.save()
                return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        try:
            jugador = Jugador.objects.get(id=id)
            jugador.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'POST':
        try:
            serializador = JugadorSerializer(data=request.data)
            if serializador.is_valid():
                serializador.save()
                return Response(serializador.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)    
        except:
            return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)