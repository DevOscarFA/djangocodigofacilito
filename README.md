# ejecutar instruccciones

## crear un proyecto
docker-compose run --rm web django-admin.py startproject {NOMBRE_PROYECTO} .

## crear un usuario
docker-compose run --rm web python manage.py createsuperuser
nota Superuser creation skipped due to not running in a TTY. You can run `manage.py createsuperuser` in your project to create one manually.

## crear una aplicacion
docker-compose run --rm --workdir="/webapp/apps" web django-admin.py startapp {NOMBRE_APLICACION}

## ver paquetes instalados de django
pip freeze

## realizar las migraciones
docker-compose run --rm web python manage.py migrate

https://www.pgadmin.org/download/pgadmin-4-container/

docker-compose run --rm --workdir="/webapp/apps" web django-admin.py startapp
--workdir="/var/www/html/TestPhalcon"

## configuracion de settings


INSTALLED_APPS = [
    'apps.adopcion',
    'apps.mascota',
]

## ejecutar migraciones

docker-compose run --rm web python manage.py makemigrations
docker-compose run --rm web python manage.py migrate

##url y vista