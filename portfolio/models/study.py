from django.db import models
from datetime import datetime
from .user import User
from .company import Company
from django.contrib import admin


class Study(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=350)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=None)
    image_url = models.CharField(max_length=255)


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "company",
        "title",
        "description",
        "start_date",
        "end_date",
        "image_url",
    )
