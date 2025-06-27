from .base import *  # noqa

DEBUG = False

MIDDLEWARE.insert(  # noqa
    1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

STATIC_ROOT = BASE_DIR / "static"  # noqa

STATIC_URL = "/static/"

STORAGES.update(  # noqa: F405
    {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
        },
    }
)
