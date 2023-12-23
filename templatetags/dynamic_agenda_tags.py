from django.db.models import Max
from django import template
from django_dynamic_agenda.models import AgendaItem, AgendaGroup

register = template.Library()

@register.inclusion_tag('django_dynamic_agenda/agenda_items.html')
def show_agenda(group_name=None, items_limit=None):

    # Convert limit to integer and it not convertible to int then default to none
    try:
        if items_limit:
            items_limit = int(items_limit)
    except ValueError:
        items_limit = None

    if group_name:
        items = AgendaItem.objects.filter(group__name=group_name).order_by('-created')
    else:
        latest_group = AgendaGroup.objects.annotate(
            latest_date=Max('items__created')
        ).order_by('-latest_date').first()

        if latest_group:
            items = latest_group.items.all().order_by('-created')
        else:
            items = AgendaItem.objects.none()

    # Apply limit to the queryset if a limit parameter is specified and is an integer
    if items_limit:
        items = items[:items_limit]

    return {'items': items}