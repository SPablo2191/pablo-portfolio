from django.db import models
from .user import User


class Technology(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    image_url = models.TextField(max_length=255)
