from typing import Any

from django.views.generic import TemplateView
from helpers.mixins import HxTemplateMixin


class IndexView(HxTemplateMixin, TemplateView):
    template_name = "landing/htmx/index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({"title": "Inicio"})
        return context
