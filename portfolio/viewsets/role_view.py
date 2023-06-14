from rest_framework import viewsets
from ..models.role import Role,RoleSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer