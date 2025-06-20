from typing import Any

from apps.events.models import Events, SpecialEvents
from apps.landing.models import AboutUs
from django.utils import timezone
from django.views.generic import TemplateView
from helpers.mixins import HxTemplateMixin

# today_start = datetime.combine(date.today(), datetime.min.time())


class IndexView(HxTemplateMixin, TemplateView):
    template_name = "landing/htmx/index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": "Inicio",
                "about": AboutUs.objects.last(),
                "events": Events.objects.filter(
                    start_time__gte=timezone.now()
                ),
                "special_events": SpecialEvents.objects.filter(
                    date__gte=timezone.now()
                ),
            }
        )
        return context
