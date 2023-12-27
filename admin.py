from django.contrib import admin
from .models import Event, TimeTable

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'shortcode_display')
    list_filter = ('start_date',)  
    readonly_fields = ('shortcode_display',)
    
    def shortcode_display(self, obj):
        return obj.generate_shortcode()
    shortcode_display.short_description = "Display Tag"

@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('item_event', 'start_time', 'created', 'description')
    list_filter = ('item_event', 'start_time', 'created')