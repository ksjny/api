## Welcome!

## Setup

* Clone project
  * `$ git clone`
* Create and activate a virtual environment
  * `$ pip3 install virtualenv`
  * `$ python3 -m virtualenv venv`
  * `$ source venv/bin/activate`
* Install python dependencies
  * `$ pip3 install -r requirements.txt`
* Install postgresql
  * `$ sudo apt-get install postgresql`
  * `$ sudo apt-get update`
* Create project database
  * `$ sudo -i -u postgres`
  * `$ psql`
  * `postgres=# create database <database_name>;`
  * `postgres=# \connect <database_name>;`
* Create development user
  * `<database_name>=# create user <username> password <password> with superuser;`
* Create secret_settings.py under /nwhacks, example below
    ```python
    SECRET_KEY = '<secret_key>'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '<database_name>',
            'USER': '<username>',
            'PASSWORD': '<password>',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

    DEBUG = True
    ```

* Run the server
  * `$ python manage.py runserver`
* Or run the tests
  * `$ python manage.py test`
