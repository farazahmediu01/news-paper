# Newspaper App

A Django-based newspaper application where users can sign up, log in, create articles, and leave comments. Built with Django's class-based views and containerized with Docker.

## Features

- **User Authentication** — Custom user model with age field, signup, login, logout, and password reset via email
- **Articles** — Create, read, update, and delete articles (only authors can edit/delete their own)
- **Comments** — Authenticated users can comment on any article
- **Bootstrap 5 UI** — Styled with django-crispy-forms and Bootstrap 5
- **Static Files** — Served with WhiteNoise (no need for Nginx in development)

## Tech Stack

- Python 3.13
- Django 5.0
- SQLite (default)
- uv (package manager)
- Docker
- WhiteNoise (static files)
- django-crispy-forms + Bootstrap 5
- environs (environment variable management)

## Getting Started

### Run with Docker

```bash
docker build -t news-paper .
docker run -p 8000:8000 -e SECRET_KEY="your-secret-key" news-paper
```

The container automatically runs migrations on startup, then starts the server at `http://localhost:8000`.

### Run Locally

```bash
uv sync
```

Create a `.env` file in the project root:

```
SECRET_KEY=your-secret-key
```

Then run:

```bash
uv run python manage.py migrate
uv run python manage.py runserver
```

## Project Structure

```
news-paper/
├── django_project/     # Project settings, root URL config, WSGI
├── accounts/           # Custom user model (AbstractUser + age field), signup view
├── articles/           # Article & Comment models, full CRUD views
├── pages/              # Static pages (home)
├── templates/          # All HTML templates (base, articles, registration)
├── static/             # Static assets (CSS, JS)
├── Dockerfile          # Container config
├── .dockerignore       # Files excluded from Docker build
└── pyproject.toml      # Dependencies managed by uv
```

## Available Routes

| Route | Description |
|---|---|
| `/` | Home page |
| `/accounts/signup/` | User registration |
| `/accounts/login/` | Login |
| `/accounts/logout/` | Logout |
| `/accounts/password_reset/` | Password reset flow |
| `/articles/` | List all articles (login required) |
| `/articles/new/` | Create new article |
| `/articles/<id>/` | Article detail + comments |
| `/articles/<id>/edit/` | Edit article (author only) |
| `/articles/<id>/delete/` | Delete article (author only) |
| `/admin/` | Django admin panel |

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `SECRET_KEY` | Yes | Django secret key |

## Lessons Learned During Dockerization

### Linux is case-sensitive, Windows is not
Renaming `Templates/` to `templates/` worked locally on Windows but broke inside the Docker container (Linux). Django couldn't find any templates, resulting in 500 errors on every page. Git on Windows also doesn't detect case-only renames — a two-step rename is required:
```bash
git mv Templates temp_templates && git mv temp_templates templates
```

### `runserver` must bind to `0.0.0.0` inside a container
Django's `runserver` defaults to `127.0.0.1`, which is only accessible inside the container. To expose it to the host machine, bind to `0.0.0.0:8000`.

### Environment variables don't exist at build time
`SECRET_KEY` is loaded from the environment via `environs`. Since `.env` is excluded by `.dockerignore`, the key must be passed at runtime with `-e`, not during `docker build`. This also means any commands that need Django settings (like `migrate`) must run at container startup, not in the Dockerfile's `RUN` step.

### `.dockerignore` is essential
Without it, unnecessary files like `.venv/`, `.git/`, `db.sqlite3`, and `__pycache__/` get copied into the image, increasing its size and potentially causing conflicts.

### `EXPOSE` is documentation, not configuration
`EXPOSE 8000` in a Dockerfile doesn't publish the port. The actual port mapping happens at runtime with `docker run -p 8000:8000`. `EXPOSE` just tells others which port the app uses.

### Port conflicts mean a container is already running
`port is already allocated` means another container is using that port. Use `docker ps` to find it and `docker stop <id>` to free the port.
