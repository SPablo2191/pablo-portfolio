from django.urls import path
from rest_framework import routers
from .viewsets.achievement_view import AchievementViewSet
from .viewsets.user_view import UserViewSet
from .viewsets.company_view import CompanyViewSet
from .viewsets.fact_view import FactViewSet

route = routers.SimpleRouter()
route.register("achievements", AchievementViewSet)
route.register("users", UserViewSet)
route.register("companies", CompanyViewSet)
route.register("facts", FactViewSet)
urlpatterns = route.urls
