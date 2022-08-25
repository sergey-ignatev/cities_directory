from django.db import models

from rest_framework import generics
from rest_framework import filters

from citiesDirectory.apps.external_api.serializers.v1 import ValidateQueryParams, RegionSerializer
from citiesDirectory.apps.service_regions.models import RegionDirectory


class RegionsView(
    generics.ListAPIView,
    generics.CreateAPIView
):
    """
    View for a list of Regions instances
    """
    search_fields = ["region_name"]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    serializer_class = RegionSerializer

    def get_queryset(self) -> models.QuerySet:
        """
        Searches the database in relation to the query sent by the region name.
        :return: Django queryset object containing search results.
        """
        query_params = ValidateQueryParams(data=self.request.query_params)
        query_params.is_valid(raise_exception=True)
        queryset = RegionDirectory.objects.all()
        return queryset
