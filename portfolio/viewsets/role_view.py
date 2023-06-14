from rest_framework import viewsets
from ..models.role import Role
from ..serializers.role_serializer import RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer