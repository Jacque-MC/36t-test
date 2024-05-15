from rest_framework.viewsets import ModelViewSet
from entidades.models import Maestro, Salon
from entidades.serializers import MaestroSerializer, SalonSerializer


class MaestroViewSet(ModelViewSet):
    serializer_class = MaestroSerializer

    def get_queryset(self):
        return Maestro.objects.all().order_by('nombre_completo')


class SalonViewSet(ModelViewSet):
    serializer_class = SalonSerializer

    def get_queryset(self):
        return Salon.objects.all().order_by('letra', 'codigo')
