from django.db import models
from .user import User
from django.contrib import admin
from rest_framework import serializers


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    image_url = models.CharField(max_length=255)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "image_url")


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
