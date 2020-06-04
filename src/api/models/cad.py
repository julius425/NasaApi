import typing as t

from django.db import models

from utils.models import TimeStamped


class CADRecordManager(models.Manager):

    def with_designations(self, designations):
        return self.get_queryset().filter(des__in=designations)


class CADRecord(TimeStamped):

    REQUIRED_FIELDS: t.Set[str] = {
        'des',
        'orbit_id',
        'jd',
        'cd',
        'dist',
        'dist_min',
        'dist_max',
        'v_rel',
        'v_inf',
        't_sigma_f',
        'h'}

    des = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    orbit_id = models.IntegerField(
        null=True,
        blank=True
    )
    jd = models.FloatField(
        null=True,
        blank=True
    )
    cd = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    dist = models.FloatField(
        null=True,
        blank=True
    )
    dist_min = models.FloatField(
        null=True,
        blank=True
    )
    dist_max = models.FloatField(
        null=True,
        blank=True
    )
    v_rel = models.FloatField(
        null=True,
        blank=True
    )
    v_inf = models.FloatField(
        null=True,
        blank=True
    )
    t_sigma_f = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    h = models.FloatField(
        null=True,
        blank=True
    )

    objects = CADRecordManager()
