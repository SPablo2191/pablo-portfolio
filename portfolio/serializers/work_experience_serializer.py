from rest_framework import serializers
from ..models.work_experience import WorkExperience
from .company_serializer import CompanySerializer
from .role_serializer import RoleSerializer


class WorkExperienceSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    role = RoleSerializer()
    class Meta:
        model = WorkExperience
        fields = "__all__"
