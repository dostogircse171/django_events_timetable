from django import template
from django_dynamic_agenda.models import AgendaItem

register = template.Library()

@register.inclusion_tag('django_dynamic_agenda/agenda_items.html')
def show_agenda():
    items = AgendaItem.objects.all()
    return {'items': items}
