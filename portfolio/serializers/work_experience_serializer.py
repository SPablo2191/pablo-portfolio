from rest_framework import serializers
from ..models.work_experience import WorkExperience


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ["role", "company", "description","start_date","end_date"]
