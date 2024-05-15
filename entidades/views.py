from django.db.models import Sum

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from entidades.models import Maestro, Salon
from entidades.serializers import MaestroSerializer, SalonSerializer


class MaestroViewSet(ModelViewSet):
    serializer_class = MaestroSerializer

    def get_queryset(self):
        return Maestro.objects.all().order_by('nombre_completo')
    
    @action(detail=False, methods=('get',))
    def sueldos(self, request):
        response = {
            "sueldos": Maestro.objects.all().aggregate(sueldos=Sum('sueldo'))['sueldos']
        }
        return Response(response, status=status.HTTP_200_OK)


class SalonViewSet(ModelViewSet):
    serializer_class = SalonSerializer

    def get_queryset(self):
        return Salon.objects.all().order_by('letra', 'codigo')
