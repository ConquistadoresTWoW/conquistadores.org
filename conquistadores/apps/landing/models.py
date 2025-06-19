from django.db import models
from helpers.models import BaseModel


class AboutUs(BaseModel):
    slogan = models.CharField(verbose_name="Slogan", max_length=75)

    def __str__(self):
        return "Sección: Quienes Somos"

    class Meta:
        verbose_name = "Quién Somos"
        verbose_name_plural = "Quiénes Somos"


class AboutUsCard(BaseModel):
    about_us = models.ForeignKey(
        AboutUs, on_delete=models.CASCADE, related_name="card"
    )
    title = models.CharField(verbose_name="Título", max_length=20)
    description = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Card Sección Quien Somos"
        verbose_name_plural = "Card Sección Quien Somos"
