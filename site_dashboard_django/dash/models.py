from asyncio.windows_events import NULL
from itertools import product
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.core.exceptions import ValidationError

from datetime import datetime  #---------------------------------------------------------------- Tasks
class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    number = models.IntegerField(default=0)
    def __str__(self):
        return self.name

#---------------------------------------------------------------- Projects

class Project(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    start_date = models.DateTimeField(default=datetime.now, blank=False)
    end_date = models.DateTimeField(blank=True, null=True)
    class ProjectStatus(models.TextChoices):
        NEW = 'N', _('New')
        INPROGRESS = 'I', _('InProgress')
        ENDED = 'E', _('Ended')
        CANCELED = 'C', _('Canceled')
        SUSPENDED = 'S', _('Suspended')
        

    status = models.CharField(
    max_length=2,
    choices=ProjectStatus.choices,
    default=ProjectStatus.NEW,
    )

    def __str__(self):
        return str(self.name)

class ProductBackLog(models.Model):
    name = models.CharField(max_length=30, default="PBL", blank=False)
    project = models.OneToOneField(
        Project,
        related_name='pbl',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    def __str__(self):
        return str(self.name)+" "+str(self.project)










class UserStory(models.Model):

    name = models.CharField(max_length=100, default="US", blank=True, null=True)
    project = models.ForeignKey(
        Project,
        related_name='us',
        on_delete=models.CASCADE,
        default=Project
    )
    product_back_log = models.ForeignKey(
        ProductBackLog,
        related_name='us',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=Project.pbl
    )
    theme = models.CharField(max_length=100, blank=True, null=True)
    as_a = models.CharField(max_length=100, blank=True, null=True)
    i_want = models.CharField(max_length=100, blank=True, null=True)
    in_order_to = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class UsPriority(models.TextChoices):
        WEAK = 'W', _('Weak')
        MEDIUM = 'M', _('Medium')
        STRONG = 'S', _('Strong')
    priority = models.CharField(
    max_length=2,
    choices=UsPriority.choices,
    default=UsPriority.MEDIUM,
    )

    class UsStatus(models.TextChoices):
        NEW = 'N', _('New')
        INPROGRESS = 'I', _('InProgress')
        ENDED = 'E', _('Ended')
        CANCELED = 'C', _('Canceled')
        SUSPENDED = 'S', _('Suspended')
    status = models.CharField(
    max_length=2,
    choices=UsStatus.choices,
    default=UsStatus.NEW,
    )

    
    def clean(self):
        self.is_cleaned = True
        if self.product_back_log is not None:
            if self.project != self.product_back_log.project:
                raise ValidationError("my error message "+str(self.project)+ " "+str(self.product_back_log.project))
            super(UserStory, self).clean()

    def save(self, *args, **kwargs):
        if not self.is_cleaned:
            self.full_clean()
        super(UserStory, self).save(*args, **kwargs)

    def __str__(self):
        if self.product_back_log is not None:
            return str(self.name)+" "+str(self.product_back_log)
        else:
            return str(self.name)
