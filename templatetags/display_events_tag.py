from django.db.models import Max
from django import template
from django_events_timetable.models import TimeTable, Event
from django_events_timetable.utils import days_to_date

register = template.Library()

def calculate_days_until_event(event):
    """ Calculate days until the event and check if it's negative. """
    days_until_event = days_to_date(event.start_date)
    is_negative = days_until_event < 0
    return abs(days_until_event) if is_negative else days_until_event, is_negative

@register.inclusion_tag('django_events_timetable/event_items.html')
def display_event(event_id=None, items_limit=None):
    """ Display events based on the event ID and items limit, 
        or a message if the ID is not found. """

    try:
        items_limit = int(items_limit) if items_limit else None
    except ValueError:
        items_limit = None

    # Initialize variables
    days_until_event = None
    is_negative = False
    message = None

    if event_id:
        try:
            event = Event.objects.get(pk=event_id)
            items = event.items.order_by('start_time')
            days_until_event, is_negative = calculate_days_until_event(event)
        except Event.DoesNotExist:
            items = []
            message = f"Event ID-{event_id} not found"
    else:
        latest_event = Event.objects.annotate(
            latest_date=Max('items__created')
        ).order_by('-latest_date').first()

        if latest_event:
            items = latest_event.items.order_by('start_time')
            days_until_event, is_negative = calculate_days_until_event(latest_event)
        else:
            items = TimeTable.objects.none()

    if items_limit:
        items = items[:items_limit]

    return {'items': items, 'days_until_event': days_until_event, "is_negative": is_negative, 'message': message}