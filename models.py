from django.db import models

class Event(models.Model):
    LIGHT = 'dj_timetable_light'
    DARK = 'dj_timetable_dark'
    CUSTOM = 'dj_timetable_custom'

    THEME_CHOICES = [
        (LIGHT, 'Light'),
        (DARK, 'Dark'),
        (CUSTOM, 'Custom'),
    ]

    name = models.CharField(max_length=100, verbose_name="Event Name")
    start_date = models.DateField(help_text="Date when the Event is schedule for.", verbose_name="Event Date")
    theme_color = models.CharField(max_length=20, choices=THEME_CHOICES, default=LIGHT, verbose_name="Theme Color", help_text="How the event section will look when display on any page")
    #For Theme Color
    primary_color = models.CharField(max_length=7, default='#FF8494', help_text="Primary color in hexadecimal or RGB or ColorName format (Eg. #FF8494 or rgb(23,23,12) or green/red/blue)", verbose_name="Primary Color")
    background_color = models.CharField(max_length=7, default='#FFFFFF', help_text="Background color in hexadecimal or RGB or ColorName format (Eg. #FF8494 or rgb(23,23,12) or green/red/blue)", verbose_name="Background Color")
    text_color = models.CharField(max_length=7, default='#000000', help_text="Text color in hexadecimal or RGB or ColorName format (Eg. #FF8494 or rgb(23,23,12) or green/red/blue)", verbose_name="Text Color")
    
    def generate_shortcode(self):
        """Generate a shortcode for template inclusion tag."""
        return f'{{% display_event "{self.id}" %}}'

    def __str__(self):
        return f"{self.name} - {self.start_date.strftime('%Y-%m-%d')}"

    class Meta:
        unique_together = [('name', 'start_date')]
class TimeTable(models.Model):
    item_event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='items', verbose_name="Event Name")
    start_time = models.TimeField(verbose_name="Start Time", help_text="When this will start")
    end_time = models.TimeField(verbose_name="End Time", help_text="When this will end", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    title =models.CharField(max_length=70, verbose_name="Whats happening", help_text="What is happening in this time?")
    description = models.TextField(verbose_name="Description", help_text="Useful description about this time event.", blank=True, null=True)

    def __str__(self):
        return f"{self.start_time} - {self.description}"
    class Meta:
        ordering = ['start_time']

# Specific for Django CMS
try:
    from cms.models.pluginmodel import CMSPlugin
    CMS_IS_INSTALLED = True
    
except ImportError:
    CMS_IS_INSTALLED = False

if CMS_IS_INSTALLED:
    class EventPluginModel(CMSPlugin):
        event = models.ForeignKey('django_events_timetable.Event', on_delete=models.CASCADE)

        def __str__(self):
            return self.event.name
