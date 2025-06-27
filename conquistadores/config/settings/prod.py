from .base import *  # noqa

DEBUG = False

INSTALLED_APPS += [  # noqa
    "whitenoise.runserver_nostatic",
]

MIDDLEWARE.insert(  # noqa
    1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

STATIC_URL = "static/"

STORAGES.update(  # noqa: F405
    {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
        },
    }
)

STATIC_ROOT = BASE_DIR / "static"  # noqa: F405
