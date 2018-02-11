from django.contrib.gis.db import models


class PointOfInterest(models.Model):

    name = models.CharField(max_length=255)
    point = models.PointField(srid=4326)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = 'point of interest'
        verbose_name_plural = 'points of interest'