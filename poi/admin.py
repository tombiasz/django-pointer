from django.contrib import admin

from .models import PointOfInterest


class PointOfInterestAdmin(admin.ModelAdmin):
    pass

admin.site.register(PointOfInterest, PointOfInterestAdmin)