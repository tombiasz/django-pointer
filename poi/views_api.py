from rest_framework import generics

from .models import PointOfInterest
from .serializers import PointOfInterestSerializer


class PointOfInterestListView(generics.ListAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer
