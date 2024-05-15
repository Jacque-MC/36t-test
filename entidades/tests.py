from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from entidades.models import Maestro
from entidades.serializers import MaestroSerializer
from entidades.views import MaestroViewSet


class MaestroTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
    
    def test_list(self):
        """
        Test lista de maestros
        """
        request = self.factory.get("/maestros/")
        response = MaestroViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        """
        Test creación de maestros con un salón
        """
        data = {"nombre_completo": "Luis Rodriguez",
                "sueldo": 2500.00, 
                "salones": [
                    {"letra": "A", "codigo": "COD"}
                ]}
        serializer = MaestroSerializer(data=data)

        self.assertTrue(serializer.is_valid())

        request = self.factory.post("/maestros/", data, format="json")
        response = MaestroViewSet.as_view({'post': 'create'})(request)

        self.assertEqual(response.status_code, 201)

    def test_limit_salones(self):
        """
        Test creación de maestro con más de tres salones
        """
        data = {"nombre_completo": "Luis Rodriguez",
                "sueldo": 2500.00, 
                "salones": [
                    {"letra": "A", "codigo": "COD"}, 
                    {"letra": "B", "codigo": "CUE"}, 
                    {"letra": "C", "codigo": "POL"}, 
                    {"letra": "D", "codigo": "DUE"}
                ]}
        serializer = MaestroSerializer(data=data)
        self.assertFalse(serializer.is_valid())

        # 
        request = self.factory.post("/maestros/", data, format="json")
        response = MaestroViewSet.as_view({'post': 'create'})(request)

        self.assertNotEqual(response.status_code, 201)

    def test_update_limit(self):
        """
        Test modificar maestro añadiendo un salón extra sobre el límite de tres
        """
        maestro = Maestro.objects.create(nombre_completo="Luis Rodriguez", sueldo=2500.00)
        maestro.salones.create(letra="A", codigo="COD")
        maestro.salones.create(letra="B", codigo="CUE")
        maestro.salones.create(letra="C", codigo="POL")
        url = reverse("maestros-update", kwargs={'pk': maestro.pk})

        request = self.factory.put(url, {"salones": [{"letra": "D", "codigo": "DUE"}]}, format="json")
        response = MaestroViewSet.as_view({'put': 'partial_update'})(request, pk=maestro.pk)

        self.assertEqual(response.status_code, 400)
