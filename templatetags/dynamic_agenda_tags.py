from django.db.models import Max
from django import template
from django_dynamic_agenda.models import AgendaItem, AgendaGroup

register = template.Library()

@register.inclusion_tag('django_dynamic_agenda/agenda_items.html')
def show_agenda(group_name=None):
    if group_name:
        items = AgendaItem.objects.filter(group__name=group_name)
    else:
        latest_group = AgendaGroup.objects.annotate(
            latest_date=Max('items__created')
        ).order_by('-latest_date').first()

        if latest_group:
            items = latest_group.items.all()
        else:
            items = AgendaItem.objects.none()

    return {'items': items}