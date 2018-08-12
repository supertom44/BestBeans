import django_filters
from django import forms

from .models import Bean


class BeanFilter(django_filters.FilterSet):
    roasts = django_filters.MultipleChoiceFilter(choices=Bean.ROAST_LEVELS, field_name='roast_level', widget=forms.CheckboxSelectMultiple)
