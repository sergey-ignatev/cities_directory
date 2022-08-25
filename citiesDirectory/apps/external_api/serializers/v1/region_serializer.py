from rest_framework import serializers
from rest_framework import fields

from citiesDirectory.apps.service_regions.models import RegionDirectory


class ValidateQueryParams(serializers.Serializer):

    search = fields.CharField(
        required=False
    )


class RegionSerializer(serializers.ModelSerializer):
    """
    Serializer for Region model
    """

    class Meta:
        """
        Additional information on serializer
        """

        model = RegionDirectory
        fields = (
            'id', 'region_name',
        )
