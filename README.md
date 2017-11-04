# Catalog App
A basic catalog app built on Django and postgres 
## Requirements
- Django
- Postgres
- Bootstrap
- Jquery
- social-auth-app-django
## Installation And Configuration
- Clone this repo
```git clone https://github.com/juluahamed/catalog_app.git```
- Install pip
- Install , create and activate a virtual environment
- Set up the environment
``` pip install -r requirements.txt ```
- Setup the database(Postgres). View catalog_app/settings.py for configuration. [Refer this](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)
- Install Apache webserver
```sudo apt-get install apache2```
- Install mod_wsgi application handler 
```sudo apt-get install libapache2-mod-wsgi```
- Configure mod_wsgi to handle our application. For help, [Refer this](https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/modwsgi/)
- Migrate to the database
```python manage.py makemigrations```
```python manage.py migrate```
- Collect static to track the changes to the static files. Or use third party libraries to automate this process
``` python manage.py collectstatic```
- If you are hosting this on a server, set up ufw to allow only necssary ports (like ssh, port 80)

## Debugging
- Pubic IP of server is 35.154.100.41, but the application should be accessed at (http://35.154.100.41.xip.io/) and this is because application uses google oauth authentication and it does not approve public ip address as redirect uri.




