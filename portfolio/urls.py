from django.urls import path
from rest_framework import routers
from .viewsets.achievement_view import AchievementViewSet

route = routers.SimpleRouter()
route.register("achievement", AchievementViewSet)
urlpatterns = route.urls
