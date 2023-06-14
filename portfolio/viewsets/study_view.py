from rest_framework import viewsets
from ..models.study import Study
from ..serializers.study_serializer import StudySerializer


class StudyViewSet(viewsets.ModelViewSet):
    queryset = Study.objects.all()
    serializer_class = StudySerializer
