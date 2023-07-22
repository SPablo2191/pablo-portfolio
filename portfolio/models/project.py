from django.db import models
from .user import User
from .technology import Technology
from django.contrib import admin



class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=255)
    project_url = models.TextField(max_length=255,default="")
    technologies = models.ManyToManyField(Technology, through="TechnologyProject")

    def __str__(self) -> str:
        return self.title


class TechnologyProject(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class TechnologyProjectInline(admin.TabularInline):
    model = TechnologyProject


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TechnologyProjectInline]


