from django.db import models
from django_extensions.db.models import TimeStampedModel


class Email(TimeStampedModel):
    name = models.CharField(max_length=50)
    default_title = models.CharField(max_length=100)
    default_template = models.TextField()

    def __str__(self):
        return self.name


class EmailTemplate(TimeStampedModel):
    # movie_id is the object_id in mongo
    movie_id = models.CharField(max_length=24, unique=True)
    title = models.CharField(max_length=100)
    template = models.TextField()
    email = models.ForeignKey(
        Email, on_delete=models.CASCADE,
        related_name='templates'
    )
