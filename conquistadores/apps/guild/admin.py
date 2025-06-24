from apps.guild.models import (
    Guild,
    LootSystem,
    Recruitment,
    Rules,
    WoWClass,
)
from django.contrib import admin

admin.site.register(WoWClass)
admin.site.register(Recruitment)
admin.site.register(Rules)
admin.site.register(LootSystem)
admin.site.register(Guild)
