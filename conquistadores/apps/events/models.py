from django.db import models
from helpers.models import BaseTimeStampedModel


class Events(BaseTimeStampedModel):
    event_id = models.CharField(
        max_length=50, unique=True, db_index=True, null=True, blank=True
    )
    title = models.CharField(
        max_length=50, db_index=True, blank=True, null=True
    )
    leader = models.CharField(max_length=100, blank=True, null=True)
    image = models.URLField(max_length=200, blank=True, null=True)
    start = models.DateTimeField(db_index=True, blank=True, null=True)
    attendees = models.IntegerField(default=0)
    discord_channel_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ["start"]

    def __str__(self):
        if self.title:
            return self.title
