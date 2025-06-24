from django.db import models
from helpers.models import BaseModel, BaseTimeStampedModel


class Raids(BaseModel):
    raid_id = models.IntegerField(
        verbose_name="ID",
    )
    name = models.CharField(verbose_name="Raid", max_length=100)
    reference = models.CharField(
        verbose_name="Referencia", max_length=5, db_index=True
    )
    max_attendance = models.IntegerField(
        verbose_name="Máximo de jugadores", default=10
    )

    class Meta:
        verbose_name = "Raid"
        verbose_name_plural = "Raids"

    def __str__(self):
        return self.name


class Events(BaseTimeStampedModel):
    class EventType(models.TextChoices):
        RAID = "R", ("Raid")
        PVP = "P", ("PVP")
        SPECIAL = "E", ("Especial")

    raid_id = models.ForeignKey(
        Raids, on_delete=models.CASCADE, related_name="events"
    )
    event_id = models.IntegerField(verbose_name="ID", default=0)
    TYPE = models.CharField(
        verbose_name="Tipo de Evento",
        max_length=1,
        choices=EventType,
        default=EventType.RAID,
        blank=True,
        null=True,
    )
    reference = models.CharField(
        verbose_name="Referencia", max_length=6, db_index=True
    )
    description = models.CharField(
        verbose_name="Descripción", max_length=150, null=True, blank=True
    )
    start_time = models.DateTimeField(verbose_name="Inicia")
    lock_at_start_time = models.BooleanField(
        verbose_name="Cierra al Iniciar", default=False
    )
    locked = models.BooleanField(verbose_name="Cerrada", default=False)
    reservation_limit = models.IntegerField(
        verbose_name="Límite de Reservas", default=1
    )
    allow_comments = models.BooleanField(default=True)
    signups = models.IntegerField(verbose_name="Anotados", default=0)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.reference
