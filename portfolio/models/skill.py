from django.db import models
from .user import User
from .technology import Technology, TechnologySerializer
from django.contrib import admin
from rest_framework import serializers


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    name = models.TextField(max_length=100)
    technologies = models.ManyToManyField(Technology, through="TechnologyExperience")
    def __str__(self) -> str:
        return self.name+" "+self.description+" "+''.join([str(technology) for technology in self.technologies.all()])


class TechnologyExperience(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


class TechnologyExperienceInline(admin.TabularInline):
    model = TechnologyExperience


@admin.register(Skill)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TechnologyExperienceInline]


class SkillSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = Skill
        fields = ["description", "name", "technologies"]
