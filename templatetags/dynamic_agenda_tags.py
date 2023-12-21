from django import template
from dynamic_agenda.models import AgendaItem

register = template.Library()

@register.inclusion_tag('dynamic_agenda/agenda_items.html')
def show_agenda():
    items = AgendaItem.objects.all()
    return {'items': items}
