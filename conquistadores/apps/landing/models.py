from django.db import models
from helpers.models import BaseModel, BaseTimeStampedModel
from imagefield.fields import ImageField


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


class Gallery(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class GalleryImage(BaseTimeStampedModel):
    gallery = models.ForeignKey(
        Gallery, related_name="images", on_delete=models.CASCADE
    )
    image = ImageField(
        upload_to="images/",
        formats={
            "thumb": ["default", ("crop", (300, 300))],
            "desktop": ["default", ("thumbnail", (300, 225))],
        },
        auto_add_fields=True,
    )
    caption = models.CharField(
        verbose_name="Descripción", max_length=200, blank=True
    )
