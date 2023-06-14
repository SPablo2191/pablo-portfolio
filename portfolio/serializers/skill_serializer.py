from rest_framework import serializers
from ..models.skill import Skill
from ..models.technology import TechnologySerializer


class SkillSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = Skill
        fields = ["description", "name", "technologies"]
