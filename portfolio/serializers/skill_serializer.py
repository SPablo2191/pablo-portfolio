from rest_framework import serializers
from ..models.skill import Skill
from .technology_serializer import TechnologySerializer


class SkillSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = Skill
        fields = ["description", "name", "technologies"]
