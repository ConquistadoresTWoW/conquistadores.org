from .base import *  # noqa: F403

INSTALLED_APPS.insert(  # noqa: F405
    0,
    "whitenoise.runserver_nostatic",
)

INSTALLED_APPS += ["django_browser_reload"]  # noqa: F405

MIDDLEWARE.insert(  # noqa
    1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

MIDDLEWARE += [  # noqa: F405
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

STORAGES.update(  # noqa: F405
    {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }
)

STATICFILES_DIRS = [
    BASE_DIR / "static",  # noqa: F405
]

STATIC_URL = "static/"

STATIC_ROOT = env("STATIC_ROOT", default=BASE_DIR / "staticfiles")  # noqa: F405

WHITENOISE_KEEP_ONLY_HASHED_FILES = True
