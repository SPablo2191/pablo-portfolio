from rest_framework import viewsets
from ..models.work_experience import WorkExperience
from ..serializers.work_experience_serializer import WorkExperienceSerializer

class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer