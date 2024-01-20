
# Django Events Timetable (App Component)

Django Events Timetable is an app component offering easy integration with Django, Django CMS, and Wagtail CMS. It features a user-friendly interface for managing event items, customizable and responsive templates with Dark and Light themes, and a color picker for design personalization. Designed to complement any project seamlessly, it is also extendable and customizable to meet specific needs.


![Logo](https://i.ibb.co/vXV3Pfd/Screenshot-2024-01-20-at-1-17-15-am.png)
## Seamlessly integrate with both Django CMS and Wagtail to supercharge your content management experience.
![Logo](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*HrFLJCXTQrknxtdO2M6bMA.png)
## Authors

- [@dostogircse171](https://www.github.com/dostogircse171)
- [@amitmodi06](https://www.github.com/amitmodi06)

## Features

- Easy integration with Django projects, Django CMS or Wagtail CMS.
- Placeholder Plugin for Django CMS.
- Easy to Manage event items through Django admin or Wagtail CMS or Django CMS.
- Grouping of event items for different events or pages.
- Customizable display templates with 2 default Dark and Light design.
- Easy colorpicker for custom design.
- Responsive and clean design will fit any project without effecting exisiting CSS ot HTML design. 
- The app is extendable and custimizable as needed.


## 1. Installation

**1.1 Download/Clone the app repository to your django project directory**
```bash
  git clone https://github.com/dostogircse171/django_events_timetable.git
```

**1.2 Add `django_events_timetable` to Installed Apps**
Add the app to your `INSTALLED_APPS` in your Django project's `settings.py` or appropriate project settings file:
```python
   INSTALLED_APPS = [
       # Other installed apps
       'django_events_timetable',
       'wagtail.contrib.modeladmin', # Add this only if you are installing it for Wagtail CMS if not already there.
   ]
   ```
   ***Note: `wagtail.contrib.modeladmin` this is important to add under INSTALLED_APPS if you are using the app on Wagtail CMS otherwise skip.***

#### 1.3 Run Migrations
Create and apply migrations specifically for the `django_events_timetable` app:
```python
   python manage.py makemigrations django_events_timetable
   python manage.py migrate django_events_timetable
```

#### 1.4 Include CSS for Default Design
Add the following line to the `<head>` section of your base template (e.g., `base.html`) to include the default stylesheet:
```html
   <link rel="stylesheet" href="{% static 'django_events_timetable/css/styles.css' %}">
   ```
***Note: Make sure your `base.html` or appropriate file has `{% load static %}` at the beginning of the file***

## 2. How to use
**2.1 After applying migrate you will see 2 table in django admin under `EVENTS TIMETABLE` app which should look like as below depending on your project setup.**

**a) Django default project View**

![djproject](https://img001.prntscr.com/file/img001/9cvFshL9RgyXIgOrcdwNLQ.png)

**b) Django CMS project View**

![cms](https://img001.prntscr.com/file/img001/WiEpJ2X_RgW5RDwggNe7VA.png)

**c) Wagtail CMS project View**

![wagtail](https://img001.prntscr.com/file/img001/SDQ3ZlX-SSuXHIfNSLn2SA.png)

**2.2 Making Events:**
To display an event and it's timetable content you need to create an event first. Consider this event as a `Group` and under this event group you can add as many event timetable as needed. Once you create an Events it will autogenerate a template tag for example `{% display_event "ID" %}` 

![wagtail](https://i.ibb.co/WggFkwV/events-model-demo.gif)

**2.3 Events TimeTable:**
After you add events now need to add timetable under that event. For that you need to add timetable data and select appropriate events.

![wagtail](https://i.ibb.co/5R4L0tj/timetable-model-demo.gif)

**2.3 Displaying the Event:** To display the event in your templates, the app provides custom Django template tags for easy integration. For Django CMS the app provide Plugin Placeholder to drag and drop events into template.

To display agenda items in your Django templates, first load the `dynamic_agenda` template tags: 
```html
{% load display_events_tag %}
```
***Note: This is not required for Django CMS***

#### 2.3.1. To show the most recent event's items: `{% display_event %}`
#### 2.3.2 To show items from a specific event: `{% display_event "Event ID" %}` [This auto generates and can be copied from Events table "Display Tag"] ***[Replace "Event ID" with your specific event ID. You can use this tag multiple times in a single template as needed.]***

#### 2.3.3. To limit the number of event items displayed you can limit by passing  an additional parameter items_limit like `items_limit=1` here Number: 1 is the number of event item you want to display.

### Django CMS Plugin Placeholder Preview
![plugin_placeholder](https://i.ibb.co/bd4dSfd/cms-plugin.gif)

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Contributing

Contributions & ideas are always welcome! Please create an issue first before contributing so we can confirm if that is necessery or if someone else is already working on it. 

