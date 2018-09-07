from django.db import models

# Create your models here.
from django_extensions.db.fields import CreationDateTimeField


class SyncLog(models.Model):
    created = CreationDateTimeField()
    app = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    action = models.CharField(max_length=10)
    hash = models.CharField(max_length=50)
