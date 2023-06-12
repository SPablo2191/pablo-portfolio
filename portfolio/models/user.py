from django.db import models
from django.contrib import admin
from rest_framework import serializers


class User(models.Model):
    username = models.TextField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "password")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
