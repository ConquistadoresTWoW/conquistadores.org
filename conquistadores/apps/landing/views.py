from typing import Any

from apps.events.models import Events
from apps.guild.models import LootSystem, Recruitment, Rules
from apps.landing.models import Gallery
from django.utils import timezone
from django.views.generic import TemplateView
from helpers.mixins import HxTemplateMixin


class IndexView(HxTemplateMixin, TemplateView):
    template_name = "landing/htmx/index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": "Inicio",
                "events": Events.objects.filter(
                    start_time__gte=timezone.now()
                ),
                "gallery": Gallery.objects.last(),
                "recruitment": Recruitment.objects.last(),
                "rules": Rules.objects.last(),
                "loot": LootSystem.objects.last(),
            }
        )
        return context
