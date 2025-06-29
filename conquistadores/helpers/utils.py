import os
import uuid

from django.utils.deconstruct import deconstructible


@deconstructible
class RandomFileName:
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        ext = os.path.splitext(filename)[1]
        return self.path % (uuid.uuid4(), ext)
