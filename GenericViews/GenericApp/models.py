from django.db import models

# Create your models here.


class Generic(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
