from django.db import models
from django.views import generic


class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...

    # Metadata


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()
