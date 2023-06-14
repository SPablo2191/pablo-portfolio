from rest_framework import viewsets
from ..models.achievement import Achievement
from ..serializers.achievement_serializer import AchievementSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
