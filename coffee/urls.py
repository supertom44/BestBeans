from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoasterListView.as_view(), name='roasters'),
    path('roaster/<int:pk>', views.RoasterDetailView.as_view(), name='roaster-detail'),
    path('beans', views.BeansListView.as_view(), name='beans'),
    path('bean/<int:pk>', views.BeanDetailView.as_view(), name='bean-detail'),
]