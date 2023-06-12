from django.db import models
from .user import User
from datetime import datetime


class Study(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=350)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=None)
    image_url = models.CharField(max_length=255)
