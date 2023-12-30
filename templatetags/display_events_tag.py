from django.utils import timezone
from django.db.models import Max
from django import template
from django_events_timetable.models import TimeTable,Event
from django_events_timetable.utils import days_to_date

register = template.Library()

def calculate_days_until_event(event):
    """ Calculate days until the event and check if it's negative. """
    days_until_event = days_to_date(event.start_date)
    is_negative = days_until_event < 0
    return abs(days_until_event) if is_negative else days_until_event, is_negative

@register.inclusion_tag('django_events_timetable/event_items.html')
def display_event(event_name=None, items_limit=None):
    days_until_event = None
    is_negative = False
    
    try:
        if items_limit:
            items_limit = int(items_limit)
    except ValueError:
        items_limit = None

    if event_name:
        try:
            event = Event.objects.get(name=event_name)
            items = event.items.order_by('start_time')
            # Calculate days until the event
            days_until_event = days_to_date(event.start_date)
            is_negative = days_until_event<0
            if is_negative:
                days_until_event = abs(days_until_event)
        except Event.DoesNotExist:
            items = TimeTable.objects.none()
    else:
        latest_event = Event.objects.annotate(
            latest_date=Max('items__created')
        ).order_by('-latest_date').first()

        if latest_event:
            items = latest_event.items.all().order_by('start_time')
            # Calculate days until the event
            days_until_event = days_to_date(latest_event.start_date)
            is_negative = days_until_event<0
            if is_negative:
                days_until_event = abs(days_until_event)
        else:
            items = TimeTable.objects.none()

    if items_limit:
        items = items[:items_limit]

    return {'items': items, 'days_until_event': days_until_event, "is_negative":is_negative}
