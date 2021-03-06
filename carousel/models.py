# carousel/models

from django.db import models
from django.contrib.postgres.fields import JSONField


import os

from .scripts import randomword

def user_directory_path(instance, filename):
    directory = randomword(10)
    return directory + '/' + filename

class Presentation(models.Model):
    title = models.CharField( max_length=100, default='noname')
    docfile = models.FileField(upload_to=user_directory_path)
    color = models.CharField( max_length=100, default='#041199')
    json = JSONField()
    # anable / disable comments
    comments_display = models.CharField( max_length=100, default='block')
    