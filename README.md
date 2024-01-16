# Django Events Timetable (App Component)

Django Events Timetable is a reusable Django app for creating and managing dynamic agendas or event schedules. It offers an easy way to integrate dynamic event listing capabilities into any Django project, with customizable display options.

## Features

- Easy integration with Django projects.
- Manage event items through Django admin.
- Grouping of event items for different events or pages.
- Customizable display templates.
- Responsive and clean design.

## Installation

1. **Download and Install the App**

   Download/Clone the app repository to your django project directory
   ```bash
   git clone https://github.com/dostogircse171/django_events_timetable.git

2. **Add `django_events_timetable` to Installed Apps**

   Add the app to your `INSTALLED_APPS` in your Django project's `settings.py`:

   ```python
   INSTALLED_APPS = [
       # Other installed apps
       'django_events_timetable',
   ]

3. **Run Migrations**

   Create and apply migrations specifically for the django_events_timetable app:

   ```python
   python manage.py makemigrations django_events_timetable
   python manage.py migrate

4. **Include CSS for Default Design**

   Add the following line to the `<head>` section of your base template (e.g., `base.html`) to include the default stylesheet:

   ```html
   <link rel="stylesheet" href="{% static 'django_events_timetable/css/styles.css' %}">

## Usage
1. Access the Django admin panel to add or edit event time table and events.
2. Create `Events` instances for different categories of items.
3. Add `Time tables` instances and associate them with an `Events`.

## Displaying the Event

To display the event in your templates, the app provides custom Django template tags for easy integration.

### Loading Template Tags

To display agenda items in your Django templates, first load the `dynamic_agenda` template tags:
```html
{% load display_events_tag %}
```

1. To show the most recent event's items: `{% display_event %}`
2. To show items from a specific event: `{% display_event "Event ID" %}` [This auto generates and can be copied from Events table "Display Tag"]
*[Replace "Event ID" with your specific event ID. You can use this tag multiple times in a single template as needed.]
3. To limit the number of event items displayed you can limit by passing  an additional parameter items_limit like `items_limit=1` here Number: 1 is the number of event item you want to display.

Note: You can use the display_event tag multiple times on the same page with different events, or even with the same event, as needed. There is no limitation to the number of times it can be used. This flexibility allows you to tailor the display of event items to fit different sections or pages of your site.
