# ePet | єУлюбленець

## Dependencies

```bash
pipenv install
# or
python3.10 -m pipenv install
```

```bash
pipenv run python -m django --version
```

## Init

```bash
pipenv run python -m django startproject ePet
```

## Apps

```bash
pipenv run python manage.py startapp index
pipenv run python manage.py startapp accounts
pipenv run python manage.py startapp pets
```

## Migrations

```bash
pipenv run python manage.py makemigrations pets
pipenv run python manage.py migrate
```

## Admin

```bash
pipenv run python manage.py createsuperuser
```

## Run (dev)

```bash
pipenv run python manage.py runserver
```

## Usefull links

- 500.000+ Open-licensed SVG Vector and Icons https://www.svgrepo.com/
- Bootstrap Docs https://getbootstrap.com/docs/5.2/getting-started/introduction/
- Bootstrap Examples https://getbootstrap.com/docs/5.2/examples/
- Django Tutorial https://docs.djangoproject.com/en/5.0/intro/tutorial03/
- Django Login, Logout, Signup, Password Change, and Password Reset https://learndjango.com/tutorials/django-login-and-logout-tutorial
