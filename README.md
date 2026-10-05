# Philos

**Read the books that shaped civilization.** Philos is a social network for readers of philosophy and history,
the way Letterboxd is one for film. Members log what they read, rate and review the classics, keep a reading diary,
follow other readers and build reading lists. Anyone, signed in or not, can browse thinkers, works, schools of
thought, the big questions and a timeline covering 2,500 years.

> 🇧🇷 **Resumo:** Philos é uma rede social de filosofia e história (em inglês), no estilo do Letterboxd. Para rodar
> localmente, siga o "Quick start" abaixo. Para publicar na internet, veja "Deploy" (o Render tem plano grátis e
> o arquivo `render.yaml` já está pronto). A seção "Growth playbook" explica como o site foi preparado para gerar
> tráfego orgânico (SEO).

## What's inside

| | |
|---|---|
| **Catalogue** | 95 thinkers, 132 works, 77 sourced quotes, 36 schools, 13 branches, 6 eras. Covers Chinese, Indian, Greek, Roman, Islamic, Jewish, European, African-American, Caribbean and Japanese traditions, plus the great historians. Every work has a summary, a description and three key ideas. |
| **Social** | Read, like and to-read toggles, half-star ratings, diary entries with reviews, likes and replies on reviews, follows, an activity feed, reading lists (ranked or unranked) with likes and "you've read X%" progress, favourite works on profiles, and "read by people you follow" on work pages. |
| **Discovery** | Filterable browse (era, branch, school, difficulty, free to read), "popular this week", "if you liked this", thinker influence graph (influenced by / influenced), timeline, quote of the day, and 10 editorial reading paths ("Philosophy 101", "The Stoic Shelf"…). |
| **Onboarding** | After signup, new members tick the classics they've already read and pick a reading path. |
| **SEO** | Server-rendered pages with descriptive titles and meta descriptions, canonical URLs, Open Graph and Twitter cards, JSON-LD (`Book`, `Person`, `Review`, `WebSite` with `SearchAction`), `sitemap.xml` (works, thinkers, eras, schools, branches, quotes, lists, reviews) and `robots.txt`. |
| **Design** | Dark "ink" theme with a parchment light theme, typographic book covers generated in CSS (no image licensing), responsive down to phone width. Every form works without JavaScript; JS only makes interactions instant. |

## Tech

Django 5.2 (Python 3.11+), server-rendered templates, vanilla JS, SQLite locally and Postgres in production,
WhiteNoise for static files and gunicorn. No build step and no frontend framework.

```
accounts/   custom User (display name, bio, favourites), signup, settings
catalog/    Era, School, Topic, Thinker, Work, Quote + browse pages; seed data in catalog/seed/
social/     UserWork (read/like/rating), Entry (diary/review), likes, comments, follows, lists, feed
core/       home, search, onboarding, about, sitemap, robots.txt, template tags
templates/  all HTML;  static/  CSS, JS, favicon, Open Graph image
```

## Quick start

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
export DJANGO_DEBUG=1
python manage.py migrate
python manage.py seed_catalog          # loads the catalogue and editorial lists (safe to re-run)
python manage.py createsuperuser       # for /admin/
python manage.py runserver             # http://127.0.0.1:8000
```

Optional: `python manage.py seed_demo` creates a few `demo_*` members with ratings, reviews and follows so you
can see the social features populated. It is for local development only: it refuses to run with DEBUG off, and
`seed_demo --clear` removes the demo members again. **Don't run it on the live site.** Fake reviews mislead real
visitors.

Run the tests with `python manage.py test`.

## Deploy

All settings come from environment variables (see `.env.example`). The ones you need:

| Variable | Example |
|---|---|
| `DJANGO_SECRET_KEY` | a long random string |
| `DJANGO_ALLOWED_HOSTS` | `philos.example.com` |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | `https://philos.example.com` |
| `SITE_URL` | `https://philos.example.com` (used for canonical links, Open Graph and the sitemap) |
| `DATABASE_URL` | `postgres://…` |

**Render (free tier):** push this repo to GitHub, then on Render choose *New → Blueprint* and select it.
`render.yaml` creates the web service and a Postgres database. After the first deploy, set `SITE_URL` to your real
URL. **Docker:** `docker build -t philos . && docker run -p 8000:8000 --env-file .env philos`. **Heroku-style
hosts:** a `Procfile` is included; its release phase runs migrations and `seed_catalog`.

Production also needs email for password resets: set the `EMAIL_*` variables. For analytics, set
`PLAUSIBLE_DOMAIN` or `GA_MEASUREMENT_ID`.

## Growth playbook

The site is built to earn organic traffic. To make the most of it:

1. **Use a real domain and submit the sitemap.** Set `SITE_URL`, then add the site to Google Search Console and
   Bing Webmaster Tools and submit `https://your-domain/sitemap.xml`.
2. **Target long-tail searches.** Each work, thinker, school, branch and quote has its own page with a title that
   matches how people search, such as "Meditations by Marcus Aurelius — reviews, summary & key ideas" or
   "Stoicism: key thinkers and books". Editorial lists cover queries like "where to start with philosophy".
   Adding more works and lists in `/admin/` (or in `catalog/seed/`) adds more pages for search engines to find.
3. **User reviews are fresh content.** Every review gets an indexable page with `Review` structured data.
   Encourage reviews through onboarding, the "write the first review" prompts and the lists.
4. **Make it shareable.** Quote pages, lists and reviews all have share buttons and Open Graph cards. Post the
   daily quote (it rotates automatically) on social media with a link back to its quote page.
5. **Seed the community honestly.** Invite philosophy students, teachers, book clubs and subreddits, and write
   the first reviews and lists yourself under your own name.

Next steps worth building: per-work Open Graph images, email digests ("what your friends read this week"),
reading challenges/goals, translations of the UI, and an import from Goodreads CSV.

## Content notes

The catalogue text (biographies, summaries, key ideas) was written for Philos. Quotes are attributed to their
source work, or to a named source when the work isn't catalogued. "Read free" links go to a Project Gutenberg
search and only appear for works marked public domain. Dates for ancient figures are approximate and marked as
such.
