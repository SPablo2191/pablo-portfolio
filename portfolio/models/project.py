from django.db import models
from .user import User
from .technology import Technology
from django.contrib import admin
from rest_framework import serializers


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=255)
    technologies = models.ManyToManyField(Technology, through="TechnologyProject")


class TechnologyProject(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class TechnologyProjectInline(admin.TabularInline):
    model = TechnologyProject


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TechnologyProjectInline]


class TechnologyProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyProject
        fields = ["technology"]


class ProjectSerializer(serializers.ModelSerializer):
    technologies = TechnologyProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "user", "title", "description", "technologies"]
