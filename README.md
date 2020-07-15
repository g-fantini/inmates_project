# Inmates App

Lunch the application:
```
$ cd inmates 

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py runserver
```

Create SuperUser:
```
$ python manage.py createsuperuser
```
Is now possible to log-in using the superuser credentials at: http://localhost:8000/admin

Please visit the [User Guide](docs/userguide.md) for a complete application overview.
