from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models.project import Project, ProjectSerializer, TechnologyProject


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = serializer.save()

        technologies = request.data.get('technologies', [])
        for technology_id in technologies:
            TechnologyProject.objects.create(technology_id=technology_id, project=project)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)