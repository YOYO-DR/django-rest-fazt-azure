#para ejecutar en el azure en el despliegue
python manage.py migrate
gunicorn  config.wsgi
#ejecutar en el ssh del servidor por si hay un error 500
python manage.py collectstatic

