# Django Refresher

A basic django apllication that I used to refresh up on core concepts of Django and Django Restframework.

The project is a web-system for users to publish stories using a collection of Rest APIs.

This project will be updated as needed and should only be treated as a sample.

## Features

1. Rest API
2. PostgreSQL Database
3. Logged in File
4. Custom Permission Classes

## Setup

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
11. Create the necessary migrations:    `./manage.py makemigrations`
12. Migrate the database:   `./manage.py migrate`
13. Create a new `SuperUser` for the system using:  `./manage.py createsuperuser`
14. Start the server:   `./manage.py runserver`

_The environment file can be obtained upon request to the author._

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
```

## Documentation

The [Postman Documentation](https://documenter.getpostman.com/view/17779018/Uz5JHayD) for the project can be found at the embedded link.

## Author(s)

1. [Arkiralor](https://www.github.com/Arkiralor)
