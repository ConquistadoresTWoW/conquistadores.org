from apps.landing.views import (
    IndexView,
)
from django.urls import path

app_name = "landing"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
