from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from .views_api import PointOfInterestListView, PointOfInterestDetailsView


urlpatterns = {
    path(r'<int:pk>/', PointOfInterestDetailsView.as_view(), name="poi-details"),
    path(r'', PointOfInterestListView.as_view(), name="poi-list"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
