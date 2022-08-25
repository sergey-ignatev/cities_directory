from django.db import models


class RegionDirectory(models.Model):

    region_name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Region name',
    )


