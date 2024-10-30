from django.db import models
from django.core import validators

# Create your models here.

class Font(models.Model):
    title = models.CharField(max_length=255, validators=[validators.MinLengthValidator(limit_value=2)])
    context = models.TextField(validators=[validators.MinLengthValidator(limit_value=3)])