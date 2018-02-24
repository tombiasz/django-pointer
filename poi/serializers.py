from rest_framework_gis import serializers

from .models import PointOfInterest


class PointOfInterestSerializer(serializers.GeoModelSerializer):

    class Meta:
        model = PointOfInterest
        fields = ('id', 'name', 'point', 'created_at', 'updated_at')
