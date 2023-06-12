from django.db import models
from .user import User
from django.contrib import admin
from rest_framework import serializers

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=255)
    image_url = models.CharField(max_length=300)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "description", "image_url")

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'