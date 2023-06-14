from django.db import models
from django.contrib import admin
from .user import User


class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)

    def __str__(self) -> str:
        return self.name


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("user", "name")
