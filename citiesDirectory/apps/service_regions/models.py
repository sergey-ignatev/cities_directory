from django.db import models


class RegionDirectory(models.Model):
    """
    Basic model for storing regions
    """

    region_name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Region name',
    )


