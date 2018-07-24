from django.shortcuts import render

from django.views import generic

from coffee.models import Roaster, Bean


class RoasterListView(generic.ListView):
    model = Roaster


class RoasterDetailView(generic.DetailView):
    model = Roaster


class BeansListView(generic.ListView):
    model = Bean


class BeanDetailView(generic.DetailView):
    model = Bean


