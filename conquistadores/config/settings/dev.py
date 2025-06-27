from .base import *  # noqa: F403

DEBUG = True

INSTALLED_APPS += ["django_browser_reload"]  # noqa: F405

MIDDLEWARE += [  # noqa: F405
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

STATICFILES_DIRS = [BASE_DIR / "static"]  # noqa

STATIC_URL = "/static/"

STORAGES = {
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
