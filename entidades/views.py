from django.db.models import Count, Sum

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from entidades.models import Maestro, Salon
from entidades.serializers import MaestroSerializer, SalonSerializer


class MaestroViewSet(ModelViewSet):
    serializer_class = MaestroSerializer
    ordering_fields = ['nombre_completo', 'salones']

    def get_queryset(self):
        return Maestro.objects.all()\
            .annotate(num_salones=Count("salones"))\
                .order_by('-num_salones', 'nombre_completo')
    
    @action(detail=False, methods=('get',))
    def sueldos(self, request):
        response = {
            "sueldos": Maestro.objects.all().aggregate(sueldos=Sum('sueldo'))['sueldos']
        }
        return Response(response, status=status.HTTP_200_OK)


class SalonViewSet(ModelViewSet):
    serializer_class = SalonSerializer

    def get_queryset(self):
        code = self.request.query_params.get('codigo', None)
        salones = Salon.objects.all().order_by('letra', 'codigo')
        if code:
            salones = salones.filter(codigo__exact=code)
        return salones

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'data':serializer.data, 'objects': queryset.count()})
