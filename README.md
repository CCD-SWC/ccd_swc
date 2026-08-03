# CCD Placement Portal

Django app built for IIT Guwahati's Career Development Centre (CCD) to track interview rooms during placement and internship season.

Companies are assigned rooms; the portal helps the placement team see what's occupied and manage allocations.

## Features

- Company and room management
- Track which rooms are occupied during placement season
- Admin login for the placement team

## Setup

```bash
# Create and activate a virtual environment, then:
pip install django django-import-export

cd ccd_swc
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and sign in with the superuser account.

## Note

Academic / campus tooling project from IIT Guwahati. A personal copy also lives at [`saisandeep2484/btech-project-ccd`](https://github.com/saisandeep2484/btech-project-ccd).
