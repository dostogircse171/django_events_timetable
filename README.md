# Django Events Timetable (App Component)

Django Events Timetable is a reusable Django app for creating and managing dynamic agendas or event schedules. It offers an easy way to integrate dynamic event listing capabilities into any Django project, with customizable display options.

## Features

- Easy integration with Django projects.
- Manage agenda items through Django admin.
- Grouping of agenda items for different events or pages.
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

   Create and apply migrations specifically for the django_dynamic_agenda app:

   ```python
   python manage.py makemigrations django_events_timetable
   python manage.py migrate

4. **Include CSS for Default Design**

   Add the following line to the `<head>` section of your base template (e.g., `base.html`) to include the default stylesheet:

   ```html
   <link rel="stylesheet" href="{% static 'django_events_timetable/css/styles.css' %}">

## Usage
1. Access the Django admin panel to add or edit agenda items and groups.
2. Create `Events` instances for different categories of items.
3. Add `Time tables` instances and associate them with an `Events`.

## Displaying the Agenda

To display the agenda in your templates, the app provides custom Django template tags for easy integration.

### Loading Template Tags

To display agenda items in your Django templates, first load the `dynamic_agenda` template tags:
```html
{% load display_event %}
```

1. To show the most recent group's items: `{% display_event %}`
2. To show items from a specific group: `{% display_event "Group Name" %}` [This auto generates and can be copied from Events table "Display Tag"]
*[Replace "Group Name" with your desired group's name. You can use this tag multiple times in a single template.]
3. To limit the number of agenda display you can limit by passing  an additional parameter items_limit like `items_limit=1` here Number: 1 is the number of agenda you want to display.

Note: You can use the show_agenda tag multiple times on the same page with different groups, or even with the same group, as needed. There is no limitation to the number of times it can be used. This flexibility allows you to tailor the display of agenda items to fit different sections or pages of your site.
