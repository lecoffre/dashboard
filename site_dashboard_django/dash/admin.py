from django.contrib import admin
from dash.models import Task, Project, ProductBackLog, UserStory
# Register your models here.


admin.site.register(Project)
admin.site.register(ProductBackLog)


@admin.register(UserStory)
class TaskUserStory(admin.ModelAdmin):
    list_display = ("name", "i_want","priority")
    

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "end_date")
"""
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "status")"""