from django.db import models
from .user import User
from django.contrib import admin


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    image_url = models.CharField(max_length=255)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "image_url")
