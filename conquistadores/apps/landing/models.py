from django.db import models
from helpers.models import BaseModel, BaseTimeStampedModel
from imagefield.fields import ImageField


class Gallery(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Galería de Imagen"
        verbose_name_plural = "Galería de Imágenes"

    def __str__(self):
        return self.name


class GalleryImage(BaseTimeStampedModel):
    gallery = models.ForeignKey(
        Gallery, related_name="images", on_delete=models.CASCADE
    )
    image = ImageField(
        upload_to="images/",
        formats={
            "thumb": ["default", ("crop", (400, 300))],
        },
        auto_add_fields=True,
    )
    name = models.CharField(verbose_name="Nombre", max_length=200, blank=True)
    caption = models.CharField(
        verbose_name="Descripción", max_length=200, blank=True
    )

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imágenes"
