from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from helpers.models import BaseModel


class Guild(BaseModel):
    name = models.CharField(
        verbose_name="Nombre", max_length=150, db_index=True
    )
    description = models.CharField(verbose_name="Descripción", max_length=50)
    server = models.CharField(verbose_name="Servidor", max_length=150)
    slogan = models.CharField(verbose_name="Slogan", max_length=150)
    about = CKEditor5Field(verbose_name="Acerca de")
    active_players = models.IntegerField(
        verbose_name="Jugadores Activos", default=0
    )
    actual_progress = models.CharField(verbose_name="Servidor", max_length=150)
    active_years = models.IntegerField(verbose_name="Años Activos", default=0)
    contact = CKEditor5Field(
        verbose_name="Contacto",
        blank=True,
        null=True,
    )
    discord = models.URLField("URL de discord")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Información de la Guild"
        verbose_name_plural = "Informaciones de la Guild"


class Recruitment(BaseModel):
    cta = models.CharField(verbose_name="CTA", max_length=150, db_index=True)
    requirements = models.CharField(verbose_name="Requisitos", max_length=150)

    def __str__(self):
        return self.cta

    class Meta:
        verbose_name = "Requerimiento"
        verbose_name_plural = "Requerimientos"


class WoWClass(BaseModel):
    class Priority(models.TextChoices):
        HIGH = "H", ("Alta")
        MEDIUM = "M", ("Media")
        LOW = "L", ("Baja")

    recruitment = models.ForeignKey(
        Recruitment,
        on_delete=models.CASCADE,
        related_name="classes",
        blank=True,
        null=True,
    )
    name = models.CharField(
        verbose_name="Clase", max_length=150, db_index=True
    )
    priority = models.CharField(
        verbose_name="Prioridad",
        max_length=1,
        choices=Priority,
        default=Priority.LOW,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Clase"
        verbose_name_plural = "Clases"

    def __str__(self):
        return f"{self.recruitment}: {self.name} - {self.priority}"


class Rules(BaseModel):
    honor = models.CharField(verbose_name="Código de Honor", max_length=250)
    commitment = models.CharField(verbose_name="Compromiso", max_length=250)
    communication = models.CharField(
        verbose_name="Comunicación", max_length=250
    )
    loot = models.CharField(verbose_name="Botín", max_length=250)

    class Meta:
        verbose_name = "Regla"
        verbose_name_plural = "Reglas"

    def __str__(self):
        return "Reglas"


class LootSystem(BaseModel):
    rules = CKEditor5Field(
        verbose_name="Reglas de Loot",
        blank=True,
        null=True,
    )
    council = CKEditor5Field(
        verbose_name="Loot Council",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Sistema de Loot"
        verbose_name_plural = "Sistemas de Loot"

    def __str__(self):
        return "Sistema de Loot"
