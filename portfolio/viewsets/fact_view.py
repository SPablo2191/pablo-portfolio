from rest_framework import viewsets
from ..models.fact import Fact,FactSerializer


class FactViewSet(viewsets.ModelViewSet):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer
