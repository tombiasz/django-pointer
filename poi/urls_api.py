from django.conf.urls import url, include
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views_api import PointOfInterestListView, PointOfInterestDetailsView


urlpatterns = {
    path(r'<int:pk>/', PointOfInterestDetailsView.as_view(), name="poi-details"),
    url(r'^$', PointOfInterestListView.as_view(), name="poi-list"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
