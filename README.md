![](https://img.pngio.com/admin-dashboards-building-saas-10-matt-layman-django-png-2400_800.png)

---

# Setup Instructions

## Create new Django project
```bash
django-admin startproject <ProjectName>
```
## Run django app.
```bash
python manage.py runserver
```
## Craete new Django app.
```bash
django-admin startapp <AppName>
```

# Some Djnago jargons
> MVT
- _*Model : -*_ Models are the place in django where we have to define our database schemas.
- _*Views : -*_ Unlike other frameworks view are not used for the templates. In django view file is use for writeing our business logics.
- _*Templates : -*_ Templates are contain our frontend file which is served on web.

> DTL (_Django template language_) / ginger templates
- For using python code in html file Django uses DTL and ginger templates.

# Admin

## Access Admin panel
- for access admin panel we have to serve route with ```localhost:8000/admin``` it redirect us to admin page.

## Create admin user
- for create new admin user we have to fire a command ```python manage.py createsuperuser```.
