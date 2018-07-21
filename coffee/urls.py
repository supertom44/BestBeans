from django.urls import path

from . import views

urlpatterns = [
    path('', views.RoasterListView.as_view(), name='roasters'),
]