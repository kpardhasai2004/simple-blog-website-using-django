from django.db import models

# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()