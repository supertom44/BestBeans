from django.db import models
from taggit.managers import TaggableManager


class Roaster(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField()

    def __str__(self):
        return self.name


class Bean(models.Model):
    name = models.CharField(max_length=100)
    roaster = models.ForeignKey(Roaster, on_delete=models.CASCADE)
    country_of_origin = models.CharField(max_length=100)
    region = models.CharField(max_length=100, null=True)
    varietal = models.CharField(max_length=50, null=True)
    processing_method = models.CharField(max_length=100, null=True)
    tasting_notes = TaggableManager()

    ROAST_LEVELS = (
        ('l', 'Light'),
        ('m', 'Medium'),
        ('md', 'Medium Dark'),
        ('d', 'Dark'),
    )

    roast_level = models.CharField(max_length=2, choices=ROAST_LEVELS, help_text='Roast Level')

    def __str__(self):
        return self.name + " by " + self.roaster.name
