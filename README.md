# Django Dynamic Agenda (Component)

Django Dynamic Agenda is a reusable Django app for creating and managing dynamic agendas or event schedules. It offers an easy way to integrate dynamic event listing capabilities into any Django project, with customizable display options.

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
   git clone https://github.com/dostogircse171/django_dynamic_agenda.git

2. **Add `django_dynamic_agenda` to Installed Apps**

   Add the app to your `INSTALLED_APPS` in your Django project's `settings.py`:

   ```python
   INSTALLED_APPS = [
       # Other installed apps
       'django_dynamic_agenda',
   ]

3. **Run Migrations**

   Create and apply migrations specifically for the django_dynamic_agenda app:

   ```python
   python manage.py makemigrations dynamic_agenda
   python manage.py migrate

4. **Include CSS for Default Design**

   Add the following line to the `<head>` section of your base template (e.g., `base.html`) to include the default stylesheet:

   ```html
   <link rel="stylesheet" href="{% static 'dynamic_agenda/css/styles.css' %}">

## Usage
1. Access the Django admin panel to add or edit agenda items and groups.
2. Create `AgendaGroup` instances for different categories of items.
3. Add `AgendaItem` instances and associate them with an `AgendaGroup`.

## Displaying the Agenda

To display the agenda in your templates, the app provides custom Django template tags for easy integration.

### Loading Template Tags

To display agenda items in your Django templates, first load the `dynamic_agenda` template tags:
```html
{% load dynamic_agenda_tags %}
```

1. To show the most recent group's items: `{% show_agenda %}`
2. To show items from a specific group: `{% show_agenda "Group Name" %}` 
*[Replace "Group Name" with your desired group's name. You can use this tag multiple times in a single template.]

Note: You can use the show_agenda tag multiple times on the same page with different groups, or even with the same group, as needed. There is no limitation to the number of times it can be used. This flexibility allows you to tailor the display of agenda items to fit different sections or pages of your site.
