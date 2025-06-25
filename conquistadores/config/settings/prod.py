from .base import *  # noqa

DEBUG = False

THIRD_PARTY_APPS += [  # noqa
    "whitenoise.runserver_nostatic",
]

MIDDLEWARE.insert(  # noqa
    1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

STATIC_ROOT = BASE_DIR / "static"  # noqa

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
