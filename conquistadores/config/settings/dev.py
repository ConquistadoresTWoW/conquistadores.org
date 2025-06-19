from .base import *  # noqa: F403

DEBUG = True

SECRET_KEY = env("SECRET_KEY")  # noqa: F405

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = env("EMAIL_HOST")  # noqa: F405

EMAIL_PORT = env("EMAIL_PORT")  # noqa: F405

EMAIL_HOST_USER = env("EMAIL_HOST_USER")  # noqa: F405

EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")  # noqa: F405

EMAIL_USE_TLS = env("EMAIL_USE_TLS")  # noqa: F405

DEFAULT_FROM_EMAIL = "noreply@conquistadores.org"

INSTALLED_APPS += ["django_browser_reload"]  # noqa: F405

MIDDLEWARE += [  # noqa: F405
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

STATICFILES_DIRS = [BASE_DIR / "static"]  # noqa
