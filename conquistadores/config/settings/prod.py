from .base import *  # noqa: F403

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

MEDIA_URL = "media/"

STATIC_ROOT = env("STATIC_ROOT", default=BASE_DIR / "staticfiles")  # noqa: F405

MEDIA_ROOT = env("MEDIA_ROOT", default=BASE_DIR / "media")  # noqa: F405

WHITENOISE_KEEP_ONLY_HASHED_FILES = True
