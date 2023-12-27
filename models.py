from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from datetime import timedelta

class Event(models.Model):
    LIGHT = 'dj_timetable_light'
    DARK = 'dj_timetable_dark'

    THEME_CHOICES = [
        (LIGHT, 'Light'),
        (DARK, 'Dark'),
    ]

    name = models.CharField(max_length=100, unique=True, verbose_name="Event Name")
    start_date = models.DateField(help_text="Date when the Event is schedule for", verbose_name="Event Date")
    theme_color = models.CharField(max_length=20, choices=THEME_CHOICES, default=LIGHT, verbose_name="Theme Color", help_text="How the event section will look when display on any page")
    
    def generate_shortcode(self):
        """Generate a shortcode for template inclusion tag."""
        return f'{{% show_agenda "{self.name}" %}}'

    def __str__(self):
        return self.name
class TimeTable(models.Model):
    group = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='items')
    start_time = models.TimeField(verbose_name="Time", help_text="When this will start")
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(verbose_name="Event Description", help_text="Event activity/description what will happen at this time")

    def __str__(self):
        return f"{self.start_time} - {self.description}"
    class Meta:
        ordering = ['start_time']