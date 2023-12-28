from django.utils import timezone
from django.db.models import Max
from django import template
from django_dynamic_agenda.models import TimeTable,Event

register = template.Library()

@register.inclusion_tag('django_dynamic_agenda/agenda_items.html')
def show_agenda(event_name=None, items_limit=None):
    try:
        if items_limit:
            items_limit = int(items_limit)
    except ValueError:
        items_limit = None

    days_until_event = None

    if event_name:
        try:
            event = Event.objects.get(name=event_name)
            items = event.items.order_by('start_time')
            # Calculate days until the event
            delta = event.start_date - timezone.now().date()
            days_until_event = max(delta.days, 0)
        except Event.DoesNotExist:
            items = TimeTable.objects.none()
    else:
        latest_event = Event.objects.annotate(
            latest_date=Max('items__created')
        ).order_by('-latest_date').first()

        if latest_event:
            items = latest_event.items.all().order_by('start_time')
            # Calculate days until the event
            delta = latest_event.start_date - timezone.now().date()
            days_until_event = max(delta.days, 0)
        else:
            items = TimeTable.objects.none()

    if items_limit:
        items = items[:items_limit]

    return {'items': items, 'days_until_event': days_until_event}