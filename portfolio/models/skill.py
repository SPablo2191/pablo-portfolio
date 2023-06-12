from django.db import models
from .user import User
from .technology import Technology


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    name = models.TextField(max_length=100)
    technologies = models.ManyToManyField(Technology, through="TechnologyExperience")


class TechnologyExperience(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
