from django.shortcuts import render
from rest_framework import viewsets
from .models import Colillas, Colillero
from .serializers import ColillasSerializer, ColilleroSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

class ColillasViewSet(viewsets.ModelViewSet):
    queryset = Colillas.objects.all()
    serializer_class = ColillasSerializer

class ColilleroViewSet(viewsets.ModelViewSet):
    queryset = Colillero.objects.all()
    serializer_class = ColilleroSerializer

class RegistroDatosArduino(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = []

    def create(self, request):
        ip = request.META.get('REMOTE_ADDR')  # obtiene la ip del cliente cuando llama a la ruta
        estado = request.data.get('estado')
        
        colillero = Colillero.objects.filter(ip=ip).first()
        print(colillero)
        print(ip)
        print(estado)

        colillero.estado = estado
        colillero.save()

        return Response({

        })
       