from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Roaster(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('roaster-detail', args=[str(self.id)])


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

    def get_absolute_url(self):
        return reverse('bean-detail', args=[str(self.id)])


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bean = models.ForeignKey(Bean, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
    comments = models.TextField()

    def __str__(self):
        return self.score.__str__() + " by " + self.user.username
