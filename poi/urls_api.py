from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from .views_api import PointOfInterestListView


urlpatterns = {
    url(r'^', PointOfInterestListView.as_view(), name="poi-list"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
