from django.db import models
from django.utils.text import slugify

from utils.models import TimeStamped


class EndpointRequestPage(TimeStamped):
    """Request page model

    Model contain basic description of what will be requested,
    access methods to NASA API

    TODO: access methods
    """
    name = models.CharField(
        max_length=100
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

