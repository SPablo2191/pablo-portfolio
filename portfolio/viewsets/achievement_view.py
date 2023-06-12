from rest_framework import viewsets
from ..models.achievement import Achievement, AchievementSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
