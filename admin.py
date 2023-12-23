from django.contrib import admin
from .models import AgendaItem, AgendaGroup

admin.site.register(AgendaItem)
admin.site.register(AgendaGroup)
