from django.contrib import admin
from django_events_timetable.models import Event, TimeTable
from django_events_timetable.forms import EventAdminForm, TimeTableAdminForm

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ('id', 'name', 'start_date', 'shortcode_display')
    list_filter = ('start_date',)  
    readonly_fields = ('shortcode_display',)
    
    def shortcode_display(self, obj):
        return obj.generate_shortcode()
    shortcode_display.short_description = "Display Tag"

@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    form = TimeTableAdminForm
    list_display = ('item_event', 'start_time', 'end_time', 'created', 'title', 'description')
    list_filter = ('item_event', 'start_time', 'end_time', 'title')
