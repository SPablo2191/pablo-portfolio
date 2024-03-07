from django.db import models
from datetime import datetime
from .user import User
from .role import Role
from .company import Company
from django.contrib import admin
from rest_framework import serializers


class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=None, blank=True,null=True)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "role",
        "description",
        "start_date",
        "end_date",
    )
