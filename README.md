# Django Portfolio – pc_portfolio

A clean, dark-themed personal portfolio built with Django.

## Quickstart

```bash
# 1) Create & activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run migrations
python manage.py migrate

# 4) (Optional) Create an admin superuser
python manage.py createsuperuser

# 5) Seed your data (pulls details from your resume)
python manage.py seed_portfolio

# 6) Run the dev server
python manage.py runserver
```

Visit http://127.0.0.1:8000

## Editing Content

- Use the Django admin to manage **Profile**, **Education**, **Skill**, and **Project** entries.
- Or edit the seed data in `portfolio/management/commands/seed_portfolio.py` and re-run the command.

## Deploying
- Easiest: push to GitHub and deploy with Railway, Render, or fly.io.
- For static files in production: run `python manage.py collectstatic` and set `DEBUG=False` + proper `ALLOWED_HOSTS`.

## License
MIT