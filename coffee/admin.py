from django.contrib import admin
from .models import Roaster, Bean


class BeansInline(admin.StackedInline):
    model = Bean


@admin.register(Roaster)
class RoasterAdmin(admin.ModelAdmin):
    inlines = [BeansInline]


admin.site.register(Bean)
