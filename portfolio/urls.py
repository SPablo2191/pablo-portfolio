from django.urls import path
from rest_framework import routers
from .viewsets.achievement_view import AchievementViewSet
from .viewsets.user_view import UserViewSet

route = routers.SimpleRouter()
route.register("achievements", AchievementViewSet)
route.register("users", UserViewSet)
urlpatterns = route.urls
