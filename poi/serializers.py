from rest_framework import serializers

from .models import PointOfInterest


class PointOfInterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = PointOfInterest
        fields = ('id', 'name', 'point', 'created_at', 'updated_at')
