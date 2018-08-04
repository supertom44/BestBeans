from django.db.models import Q

from django.views import generic

from coffee.models import Roaster, Bean


class RoasterListView(generic.ListView):
    model = Roaster


class RoasterDetailView(generic.DetailView):
    model = Roaster


class BeansListView(generic.ListView):
    def get_queryset(self):
        query = self.request.GET.get('q')
        beans = Bean.objects.all()
        if query:
            beans = beans.filter(Q(name__icontains=query))
        return beans


class BeanDetailView(generic.DetailView):
    model = Bean




