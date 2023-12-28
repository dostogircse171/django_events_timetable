from django import forms
from django_events_timetable.models import Event, TimeTable

class EventAdminForm(forms.ModelForm):
    primary_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    background_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    text_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = Event
        fields = '__all__'

    class Media:
        js = ('django_events_timetable/js/event_admin.js',)

class TimeTableAdminForm(forms.ModelForm):
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)

    class Meta:
        model = TimeTable
        fields = '__all__'