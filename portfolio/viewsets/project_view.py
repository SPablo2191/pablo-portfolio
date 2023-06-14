from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models.project import Project, ProjectSerializer, TechnologyProject,TechnologyProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


