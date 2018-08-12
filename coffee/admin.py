from django.contrib import admin
from .models import Roaster, Bean, Rating


class BeansInline(admin.StackedInline):
    model = Bean


@admin.register(Roaster)
class RoasterAdmin(admin.ModelAdmin):
    inlines = [BeansInline]


admin.site.register(Bean)

admin.site.register(Rating)
