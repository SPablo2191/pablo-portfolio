from django.db import models
from .user import User
from django.contrib import admin



class Fact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    title = models.TextField(max_length=100)
    image_url = models.CharField(max_length=255,default='')

@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "description","image_url")




