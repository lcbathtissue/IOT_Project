# My Django Project

This is a Django project that takes photoresistor sensor readings from and Arduino and sends them to a Raspberry Pi using a bluetooth module and is then presented using a Django webserver.

## Project Structure

The project is structured as follows:

- **`iot_project/`**: Main project directory.
  - **`iot_app/`**: Django app directory containing the application code.
    - **`migrations/`**: Database migration files.
    - **`static/`**: Static files such as CSS, JavaScript, and images.
    - **`templates/`**: HTML templates used by the app.
    - **`__init__.py`**: Python package initializer.
    - **`admin.py`**: Django admin configurations.
    - **`apps.py`**: App configuration.
    - **`models.py`**: Database models.
    - **`tests.py`**: Unit tests.
    - **`views.py`**: Views handling HTTP requests.

- **`iot_project/`**: Django project settings and configurations.
  - **`__init__.py`**: Python package initializer.
  - **`asgi.py`**: ASGI configuration.
  - **`settings.py`**: Django project settings.
  - **`urls.py`**: Project-level URL patterns.
  - **`wsgi.py`**: WSGI configuration for deployment.

- **`manage.py`**: Django project management script.
- **`README.md`**: Project documentation.

## Code Overview

- **Database Models**: The `iot_app/models.py` file defines the data models used in the application.

- **Views**: HTTP request handling is managed by the `iot_app/views.py` file, where you can find view functions.

- **URLs**: URL patterns for the project are defined in `iot_project/urls.py`.

- **Static Files**: Static files, such as stylesheets and JavaScript scripts, are stored in the `iot_app/static/` directory.

- **Templates**: HTML templates used by the app are stored in the `iot_app/templates/` directory.

Feel free to explore the code for more details and customization options.

## Getting Started

These instructions will guide you on setting up and running the Django server on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your machine:

- Python ([Download Python](https://www.python.org/downloads/))

### Installing Dependencies

Navigate to the project directory and run the following command to install the required dependencies:

```bash
pip install django
```

### Database Migration

Run the following command to apply the initial database migrations:

```bash
python manage.py migrate
```

### Starting the Django Server

To start the Django development server, run:

```bash
python manage.py runserver
```
