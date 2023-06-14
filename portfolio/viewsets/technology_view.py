from rest_framework import viewsets
from ..models.technology import Technology
from ..serializers.technology_serializer import TechnologySerializer

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
