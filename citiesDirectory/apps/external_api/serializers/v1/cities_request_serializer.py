from rest_framework import serializers


class RegionNameSerializer(serializers.Serializer):
    """ Serializer for region """

    region_name = serializers.CharField(
        max_length=256,
        allow_blank=False,
        allow_null=False,
        required=True,
    )
