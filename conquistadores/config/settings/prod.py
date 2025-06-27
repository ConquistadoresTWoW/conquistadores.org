from .base import *  # noqa: F403

DEBUG = False

MIDDLEWARE.insert(  # noqa F405
    1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

STORAGES.update(  # noqa: F405
    {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",  # noqa: E501
        },
    }
)

STATICFILES_DIRS = [
    BASE_DIR / "static",  # noqa: F405
]

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"  # noqa: F405

WHITENOISE_KEEP_ONLY_HASHED_FILES = True
