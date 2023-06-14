from django.urls import path
from rest_framework import routers
from .viewsets.achievement_view import AchievementViewSet
from .viewsets.user_view import UserViewSet
from .viewsets.company_view import CompanyViewSet
from .viewsets.fact_view import FactViewSet
from .viewsets.technology_view import TechnologyViewSet
from .viewsets.project_view import ProjectViewSet
from .viewsets.role_view import RoleViewSet

route = routers.SimpleRouter()
route.register("achievements", AchievementViewSet)
route.register("users", UserViewSet)
route.register("companies", CompanyViewSet)
route.register("facts", FactViewSet)
route.register("technologies", TechnologyViewSet)
route.register("projects", ProjectViewSet)
route.register("roles", RoleViewSet)
urlpatterns = route.urls
