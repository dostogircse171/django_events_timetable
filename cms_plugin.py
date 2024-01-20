from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from django_events_timetable.templatetags.display_events_tag import display_event
from .models import EventPluginModel

@plugin_pool.register_plugin
class EventPluginPublisher(CMSPluginBase):
    model = EventPluginModel
    module = _("Events")
    name = _("Event Timetable")
    render_template = "django_events_timetable/event_items.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context.update(display_event(event_id=instance.event.id))
        return context