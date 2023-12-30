"""
This file contains Wagtail-specific hooks for enhancing the Wagtail admin interface.
It is only used when the app is included in a Wagtail project. These hooks have no
effect in a standard Django project without Wagtail.
"""
from .models import Event, TimeTable
from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

class EventWagtailAdmin(ModelAdmin):
    model = Event
    menu_label = 'Events'  
    menu_icon = 'date'
    list_display = ('name', 'start_date', 'shortcode_display')
    list_filter = ('start_date',)
    search_fields = ('name', 'start_date')

    def shortcode_display(self, obj):
        return obj.generate_shortcode()
    shortcode_display.short_description = "Display Tag"

class TimeTableWagtailAdmin(ModelAdmin):
    model = TimeTable
    menu_label = 'Timetable'  
    menu_icon = 'time'  
    list_display = ('item_event', 'start_time', 'end_time', 'created', 'title', 'description')
    list_filter = ('item_event__name', 'start_time', 'end_time', 'created')
    search_fields = ('title', 'start_time')

class EventTimetableGroup(ModelAdminGroup):
    menu_label = 'Events Timetable'
    menu_icon = 'folder-open-inverse'
    menu_order = 200 
    items = (EventWagtailAdmin, TimeTableWagtailAdmin)

modeladmin_register(EventTimetableGroup)