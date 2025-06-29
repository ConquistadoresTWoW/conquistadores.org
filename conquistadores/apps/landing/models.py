from django.db import models
from helpers.models import BaseModel, BaseTimeStampedModel
from imagefield.fields import ImageField


class Gallery(BaseModel):
    name = models.CharField(
        verbose_name="Nombre de la Galería de Imágenes",
        max_length=100,
        db_index=True,
    )

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
        upload_to="media/uploads/images/",
        formats={
            "thumb": ["default", ("crop", (400, 300))],
        },
        auto_add_fields=True,
    )
    name = models.CharField(verbose_name="Nombre", max_length=200, blank=True)

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imágenes"

    def __str__(self):
        return self.name
