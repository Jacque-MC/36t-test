from django.urls import path
from entidades.views import MaestroViewSet, SalonViewSet

urlpatterns = [
    path('maestros/', MaestroViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('maestros/create/', MaestroViewSet.as_view({'post': 'create'})),
    # path('maestros/<int:pk>/edit/', MaestroViewSet.as_view({'put': 'partial_update'})),
    # path('maestros/<int:pk>/delete/', MaestroViewSet.as_view({'delete': 'destroy'})),
    path('maestros/<int:pk>/', MaestroViewSet.as_view({'get': 'retrieve', 'put': 'partial_update', 'delete': 'destroy'})),
    #
    path('salones/', SalonViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('salones/create/', SalonViewSet.as_view({'post': 'create'})),
    path('salones/<int:pk>/edit/', SalonViewSet.as_view({'put': 'partial_update'})),
    path('salones/<int:pk>/delete/', SalonViewSet.as_view({'delete': 'destroy'})),
]
