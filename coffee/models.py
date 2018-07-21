from django.db import models


class Roaster(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField()