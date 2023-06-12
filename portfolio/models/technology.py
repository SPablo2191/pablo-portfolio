from django.db import models
from .user import User
from django.contrib import admin
from rest_framework import serializers


class Technology(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    image_url = models.TextField(max_length=255)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "image_url")


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = "__all__"
