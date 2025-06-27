from .base import *  # noqa

DEBUG = True

THIRD_PARTY_APPS += [  # noqa
    "whitenoise.runserver_nostatic",
]

MIDDLEWARE.insert(  # noqa
    1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

STATIC_ROOT = BASE_DIR / "static"  # noqa

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = env("EMAIL_HOST")  # noqa: F405

EMAIL_PORT = env("EMAIL_PORT")  # noqa: F405

EMAIL_HOST_USER = env("EMAIL_HOST_USER")  # noqa: F405

EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")  # noqa: F405

EMAIL_USE_TLS = env("EMAIL_USE_TLS")  # noqa: F405

DEFAULT_FROM_EMAIL = "noreply@conquistadores.org"
