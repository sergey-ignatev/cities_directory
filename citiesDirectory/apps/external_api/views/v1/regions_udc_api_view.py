from rest_framework import generics

from citiesDirectory.apps.external_api import serializers
from citiesDirectory.apps.service_regions.models import RegionDirectory


class RegionsUDCView(
    generics.UpdateAPIView,
    generics.DestroyAPIView
):
    """
    View for creating, deleting and editing of Regions
    """

    queryset = RegionDirectory.objects.all()
    serializer_class = serializers.v1.RegionSerializer
