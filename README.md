# Django Refresher

A basic django apllication that I use to refresh up on core concepts of Django and Django Restframework.

The project is a web-system for users to publish stories using a collection of Rest APIs.

_This project will be updated as needed and should only be treated as a sample._

## Features

1. [Rest API](https://restfulapi.net/)
2. [PostgreSQL Database](https://www.postgresql.org/)
3. [Logged in File](https://docs.djangoproject.com/en/4.0/topics/logging/)
4. [Custom Permission Classes](https://www.django-rest-framework.org/api-guide/permissions/)
5. [Google Maps API Integration](https://developers.google.com/maps/)

## Custom Apps

1. __`UserApp`:__ _Used for user CRUD operations to login and use the system._
2. __`StoryApp`:__ _Used for story/blog CRUD operations_
3. __`SearchApp`:__ _Used for search operations on both: stories and users_
4. __`LocationApp`:__ _Used for location CRUD operations for User Profiles_

## Screenshots

1. [The Index Page on a laptop (1366x768)](/static/assets/screenshots_for_readme/index_page_laptop.png) ![Index Page on Mobile](static/assets/screenshots_for_readme/index_page_laptop.png)
2. [The Index Page on a mobile device (1080x1920)](/static/assets/screenshots_for_readme/index_page_mobile.png) ![Index Page on Mobile](static/assets/screenshots_for_readme/index_page_mobile.png)

## Development Setup

1. Clone the repository using:  `git clone <link.git>`
2. Move into the repository directory using:    `cd DRFRefresher`
3. Create a Python virtual environment: `python -m venv env`
4. Activate the virtual environment:    `source env/scripts/activate`
5. Update `PIP` to the specified version:   `python -m pip install --upgrade pip==22.0.4`
6. Install `PIP-Tools` using:   `pip install pip-tools`
7. Compile the `requirements.in` file using:    `pip-compile`
8. Install the dependencies:    `pip install -r requirements.txt`
9. Install the `spacy` model using: `python -m spacy download en_core_web_md`
10. Copy the `.env` file to the directory root.

    - Create a `PostgreSQL` database in your machine as per the `Database Settings` in the `.env` file.
        - `PostgreSQL` setup instructions can be found [here](https://www.tutorialspoint.com/postgresql/postgresql_environment.htm).
        - `PGAdmin` is a recommended tool for managing the `PostgreSQL` database and instructions for its own setup can be found [here](https://www.pgadmin.org/download/).

11. Create the necessary migrations:    `./manage.py makemigrations`
12. Migrate the database:   `./manage.py migrate`
13. Create a new `SuperUser` for the system using:  `./manage.py createsuperuser`

    - Recommended values for `SuperUser`:

    ```shell
    - username: admin
    - email: admin@admin.com
    - password: password
    ```

14. Start the server:   `./manage.py runserver`

__NB:__ _The environment file can be obtained upon request to the author._

## .env File Format

```env
SECRET_KEY = 'some_random_32_bit__hex_key'
DEBUG = True/False
ENV_TYPE = 'DEV/PROD'

PGDATABASE = 'name_of_db'
PGHOST = 'host/url_of_db'
PGPORT = 'port_of_db'
PGUSER = 'username_for_db'
PGPASSWORD = 'password_for_db'

LANGUAGE_CODE = 'language_code'
TIME_ZONE = 'standard_time_location as city/continent'
USE_I18N = True/False
USE_TZ = True/False

USERAPP_DOCS = 'link_to_docs'
LOCATIONAPP_DOCS = 'link_to_docs'
STORYAPP_DOCS = 'link_to_docs'
SEARCHAPP_DOCS = 'link_to_docs'

## Documentation Links:
USERAPP_DOCS = ' '
LOCATIONAPP_DOCS = ' '
STORYAPP_DOCS = ' '
SEARCHAPP_DOCS = ' '

## Personal Information
LINKEDIN_PROFILE = " "

## Google Settings:
# distance_matrix, geolocation, geocoding, timezone APIs allowed
GOOGLE_API_KEY = " " 

## Email Settings:
EMAIL_HOST = ' '
EMAIL_USE_TLS = True/False
EMAIL_USE_SSL = True/False
EMAIL_PORT = int
EMAIL_HOST_USER = " "
EMAIL_HOST_PASSWORD = "Generated App Password"
```

## Documentation

The [Postman Documentation](https://documenter.getpostman.com/view/17779018/Uz5JHayD) for the project can be found at the embedded link.

## Author(s)

1. [Arkiralor](https://www.github.com/Arkiralor)
