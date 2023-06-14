from django.urls import path
from rest_framework import routers
from .viewsets.achievement_view import AchievementViewSet
from .viewsets.user_view import UserViewSet
from .viewsets.company_view import CompanyViewSet
from .viewsets.fact_view import FactViewSet
from .viewsets.technology_view import TechnologyViewSet
from .viewsets.project_view import ProjectViewSet
from .viewsets.role_view import RoleViewSet
from .viewsets.skill_view import SkillViewSet
from .viewsets.study_view import StudyViewSet
from .viewsets.work_experience_view import WorkExperienceViewSet

route = routers.SimpleRouter()
route.register("achievements", AchievementViewSet)
route.register("users", UserViewSet)
route.register("companies", CompanyViewSet)
route.register("facts", FactViewSet)
route.register("technologies", TechnologyViewSet)
route.register("projects", ProjectViewSet)
route.register("roles", RoleViewSet)
route.register("skills", SkillViewSet)
route.register("studies", StudyViewSet)
route.register("works", WorkExperienceViewSet)
urlpatterns = route.urls
