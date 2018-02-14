from mapwidgets.widgets import GooglePointFieldWidget

from django.contrib import admin
from django.contrib.gis.db import models

from .models import PointOfInterest


class PointOfInterestAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {'widget': GooglePointFieldWidget}
    }

admin.site.register(PointOfInterest, PointOfInterestAdmin)