from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField(default=0)
    def __str__(self):
        return self.name
