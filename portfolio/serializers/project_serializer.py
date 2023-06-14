from rest_framework import serializers
from ..models.project import Project
from ..models.technology import TechnologySerializer


class ProjectSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["title", "description", "technologies"]
