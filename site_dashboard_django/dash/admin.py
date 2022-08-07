from django.contrib import admin
from dash.models import Task
# Register your models here.




@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "number")