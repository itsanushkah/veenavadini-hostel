# Veena Vadini Hostel Website

A multi-page Django website for Veena Vadini hostel, with a home page, about, services, photo gallery, and a contact page.

## Features

- **Home** — landing page introducing the hostel
- **About Us** — background/info page
- **Services** — overview of services offered
- **Gallery** — dynamic photo gallery rendered from a server-side image list
- **Contact Us** — contact page for inquiries
- **Course details** — dynamic route (`/course/<courseid>`) for course-style content pages

## Tech stack

- **Backend:** Python, Django
- **Database:** SQLite (`db.sqlite3`)
- **Frontend:** Django templates (HTML/CSS), with shared `header.html` / `footer.html` / `base.html` partials

## Project structure

```
.
├── manage.py
├── db.sqlite3
├── wscubetech/          # Django project: settings, urls, views
│   ├── settings.py
│   ├── urls.py
│   └── views.py
├── templates/            # index, about us, service, gallery, contact us
├── static/                # CSS/JS assets
└── media/                 # gallery images
```

## Routes

| URL | Page |
|---|---|
| `/` | Home |
| `/about-us/` | About Us |
| `/service/` | Service |
| `/gallery/` | Gallery |
| `/contact-us/` | Contact Us |
| `/course/<courseid>` | Course details |
| `/admin/` | Django admin |

## Running locally

1. Install Django:
   ```bash
   pip install django
   ```
2. Apply migrations and run the dev server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
3. Open `http://127.0.0.1:8000`.
