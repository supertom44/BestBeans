from django.shortcuts import render

from django.views import generic

from coffee.models import Roaster


class RoasterListView(generic.ListView):
    model = Roaster


class RoasterDetailView(generic.DetailView):
    model = Roaster
