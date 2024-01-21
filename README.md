
# Django Events Timetable (App Component)

Django Events Timetable is an app component offering easy integration with Django, Django CMS, and Wagtail CMS. It features a user-friendly interface for managing event items, customizable and responsive templates with Dark and Light themes, and a color picker for design personalization. Designed to complement any project seamlessly, it is also extendable and customizable to meet specific needs.

![Logo](https://i.ibb.co/vXV3Pfd/Screenshot-2024-01-20-at-1-17-15-am.png)
[![Event Demo](https://img.shields.io/badge/-Event%20Timetable%20Demo-blue?style=for-the-badge)](https://eventdemoapp-ceaa9c531c9c.herokuapp.com/)
[![PyPi Project](https://img.shields.io/badge/-PyPi%20Project-blue?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/django-events-timetable/)



## Seamlessly integrate with both Django CMS and Wagtail to supercharge your content management experience.
![Logo](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*HrFLJCXTQrknxtdO2M6bMA.png)

## Authors
- Mohammad Golam Dostogir - [contact@dostogir.dev](mailto:contact@dostogir.dev)
- Amit Kumar - [amitmodi06@gmail.com](mailto:amitmodi06@gmail.com)

## Key Features

- **Seamless Integration**: Effortlessly integrates with Django, Django CMS, and Wagtail CMS, ensuring a smooth workflow.
- **Django CMS Compatibility**: Comes with a Placeholder Plugin specifically designed for Django CMS, enhancing content management capabilities.
- **Efficient Management**: Simplifies the management of event items through the Django admin panel, Wagtail CMS, or Django CMS, offering a user-friendly interface.
- **Organized Content**: Enables the grouping of event items, allowing for structured and organized display across different events or pages.
- **Customizable Templates**: Includes customizable display templates with two default themes: Dark and Light, catering to different aesthetic preferences.
- **Design Personalization**: Features an easy-to-use color picker, allowing for personalized design touches to match your project's theme.
- **Responsive Design**: Boasts a responsive and clean design that adapts to various devices and screen sizes, ensuring compatibility and user-friendliness without interfering with existing CSS or HTML.
- **Flexibility and Extensibility**: Designed to be extendable and customizable, meeting specific project requirements and allowing for future enhancements.


## 1. Installation
**1.1 You can install the django-events-timetable package in several ways:**

**Using Pypi**

```bash
  pip install django-events-timetable
```

**Using Poetry**

```bash
  poetry add django-events-timetable
```

**Downloading/Cloning the Repository**</br>
If you prefer, you can also download or clone the app repository directly to your Django project directory. Use the following git command to clone the repository:
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
To display an event and its timetable content you need to create an event first. Consider this event as a `Group` and under this event group you can add as many event timetables as needed. Once you create an Events it will autogenerate a template tag for example `{% display_event "ID" %}` 

![wagtail](https://i.ibb.co/WggFkwV/events-model-demo.gif)

**2.3 Events TimeTable:**
After adding an event, you need to add the timetable under that event. For that, you need to add timetable data and select appropriate events.

![wagtail](https://i.ibb.co/5R4L0tj/timetable-model-demo.gif)

**2.3 Displaying the Event:** To display the event in your templates, the app provides custom Django template tags for easy integration. For Django CMS the app provides a Plugin Placeholder to drag and drop events into the template.

To display agenda items in your Django templates, first load the `dynamic_agenda` template tags: 
```html
{% load display_events_tag %}
```
***Note: This is not required for Django CMS***

#### 2.3.1. To show the most recent event's items: `{% display_event %}`
#### 2.3.2 To show items from a specific event: `{% display_event "Event ID" %}` [This auto generates and can be copied from the "Display Tag" field of Events table] ***[Replace "Event ID" with your specific event ID. You can use this tag multiple times in a single template as needed.]***

#### 2.3.3. To limit the number of event items displayed you can limit by passing  an additional parameter items_limit like `items_limit=1` here Number: 1 is the number of event item you want to display.

### Django CMS Plugin Placeholder Preview
![plugin_placeholder](https://i.ibb.co/bd4dSfd/cms-plugin.gif)

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Contributing

Contributions & ideas are always welcome! Please create an issue first before contributing so we can confirm if that is necessary or if someone else is already working on it. 

