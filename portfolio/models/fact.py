from django.db import models
from .user import User


class Fact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    title = models.TextField(max_length=100)
