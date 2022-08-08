from django.contrib import admin
from dash.models import Task, Project, ProductBackLog, UserStory
# Register your models here.


admin.site.register(Project)
admin.site.register(ProductBackLog)
admin.site.register(UserStory)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "number")
"""
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "status")"""