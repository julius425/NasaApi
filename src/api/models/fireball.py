from django.db import models

from utils.models import TimeStamped


class FireballRecord(TimeStamped):
    date = models.DateTimeField(
        null=True,
        blank=True
    )
    energy = models.FloatField(
        null=True,
        blank=True
    )
    impact_e = models.IntegerField(
        null=True,
        blank=True
    )
    lat = models.FloatField(
        null=True,
        blank=True
    )
    lat_dir = models.CharField(
        max_length=1,
        null=True,
        blank=True,
    )
    lon = models.FloatField(
        null=True,
        blank=True
    )
    lon_dir = models.CharField(
        max_length=1,
        null=True,
        blank=True,
    )
    alt = models.FloatField(
        null=True,
        blank=True
    )
    vel = models.FloatField(
        null=True,
        blank=True
    )