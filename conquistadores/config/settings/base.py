from datetime import date
from pathlib import Path

import environ

env = environ.Env(
    ALLOWED_HOSTS=(list, []),
    CSRF_TRUSTED_ORIGINS=(list, []),
    EMAIL_HOST=(str, ""),
    EMAIL_PORT=(int, 25),
    EMAIL_HOST_USER=(str, ""),
    EMAIL_HOST_PASSWORD=(str, ""),
    EMAIL_USE_TLS=(bool, False),
    REDIS_URL=(str, None),
)
SITE_ID = 1

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

SECRET_KEY = (
    "django-insecure-9dc@ig21v&r$eq_c7m6w3re2#b0p(xy9w5u@ywd_&_=2fupkt7"
)

APPS_DIR = BASE_DIR / "apps"

DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "django_extensions",
    "django_htmx",
    "crispy_forms",
    "crispy_bootstrap5",
]

LOCAL_APPS = ["apps.landing"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {"default": env.db()}

REDIS_HOST = env("REDIS_HOST", default="redis")

REDIS_PORT = env("REDIS_PORT", default=6379)

REDIS_CACHE = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "es-es"

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

DEFAULT_CHARSET = "utf-8"

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_HOSTS_INCLUDE_SUBDOMAINS = True

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

JAZZMIN_SETTINGS = {
    "site_title": "Conquistadores Admin",
    "site_header": "Conquistadores",
    "site_brand": "Conquistadores",
    "welcome_sign": "Welcome to Conquistadores Admin",
    "copyright": f"Conquistadores {date.year}",
}

JAZZMIN_UI_TWEAKS = {"theme": "flatly"}
