from rest_framework import serializers
from ..models.work_experience import WorkExperience


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = "__all__"
