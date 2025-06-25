from typing import Any

from apps.events.models import Events
from apps.guild.models import Guild, LootSystem, Recruitment, Rules
from apps.landing.models import Gallery
from django.utils import timezone
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "landing/index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": "Inicio",
                "guild": Guild.objects.last(),
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
