from django.db import models
from .user import User


class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=255)
    image_url = models.CharField(max_length=300)
