from django.db import models
from .user import User
from django.contrib import admin
from rest_framework import serializers

class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("user", "name")

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"
