import json

from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from catalog.models import format_year

register = template.Library()


@register.filter
def stars(value):
    """Render a 1–10 half-star rating as text: 7 → '★★★½'."""
    if not value:
        return ""
    value = int(value)
    return "★" * (value // 2) + ("½" if value % 2 else "")


@register.filter
def stars_label(value):
    if not value:
        return "No rating"
    n = int(value) / 2
    return f"{n:g} star{'s' if n != 1 else ''}"


@register.filter
def halves(value):
    try:
        return f"{int(value) / 2:g}"
    except (TypeError, ValueError):
        return ""


@register.filter
def year(value, approx=False):
    return format_year(value, approx)


@register.filter
def percent(value, total):
    try:
        return round(100 * float(value) / float(total)) if total else 0
    except (TypeError, ValueError):
        return 0


@register.filter
def get_item(mapping, key):
    try:
        return mapping.get(key)
    except AttributeError:
        return None


@register.inclusion_tag("partials/cover.html")
def cover(work, size="md", link=True, show_meta=False, rating=None):
    return {"work": work, "size": size, "link": link, "show_meta": show_meta, "rating": rating}


@register.inclusion_tag("partials/avatar.html")
def avatar(user, size="md", link=True):
    return {"u": user, "size": size, "link": link}


@register.inclusion_tag("partials/thinker_avatar.html")
def thinker_avatar(thinker, size="md"):
    return {"thinker": thinker, "size": size}


@register.simple_tag
def jsonld(data):
    payload = json.dumps(data, ensure_ascii=False)
    payload = payload.replace("<", "\\u003C").replace(">", "\\u003E").replace("&", "\\u0026")
    return mark_safe(f'<script type="application/ld+json">{payload}</script>')


@register.simple_tag
def icon(name, size=18):
    """Inline SVG icons (stroke-based, inherit currentColor)."""
    paths = ICONS.get(name)
    if not paths:
        return ""
    return format_html(
        '<svg class="icon icon-{}" width="{}" height="{}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{}</svg>',
        name, size, size, mark_safe(paths),
    )


ICONS = {
    "book": '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5A2.5 2.5 0 0 1 '
            '6.5 18H20v3H6.5A2.5 2.5 0 0 1 4 20.5z"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
    "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "list": '<path d="M9 6h11M9 12h11M9 18h11"/><circle cx="4.5" cy="6" r="1"/><circle cx="4.5" cy="12" r="1"/>'
            '<circle cx="4.5" cy="18" r="1"/>',
    "search": '<circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.2-4.2"/>',
    "share": '<path d="M12 3v12M7.5 7.5L12 3l4.5 4.5"/><path d="M5 13v6.5h14V13"/>',
    "pen": '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M13.5 6.5l4 4"/>',
    "comment": '<path d="M5 5h14v10H10l-5 4z"/>',
    "repeat": '<path d="M17 3l3 3-3 3"/><path d="M4 12V9a3 3 0 0 1 3-3h13"/><path d="M7 21l-3-3 3-3"/>'
              '<path d="M20 12v3a3 3 0 0 1-3 3H4"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 '
           '12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    "moon": '<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "quote": '<path d="M9.5 7C6.5 8 5 10.5 5 14v3h5v-5H7.5c0-2 1-3.3 2.5-4zM19 7c-3 1-4.5 3.5-4.5 7v3h5v-5H17c0-2 '
             '1-3.3 2.5-4z"/>',
    "link": '<path d="M10 14a4.5 4.5 0 0 0 6.4 0l3-3a4.5 4.5 0 0 0-6.4-6.4l-1 1"/><path d="M14 10a4.5 4.5 0 0 0-6.4 '
            '0l-3 3a4.5 4.5 0 0 0 6.4 6.4l1-1"/>',
    "external": '<path d="M14 4h6v6"/><path d="M20 4l-9 9"/><path d="M18 14v6H4V6h6"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/>',
    "map": '<path d="M12 21s-6.5-6-6.5-11a6.5 6.5 0 0 1 13 0c0 5-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>',
    "calendar": '<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>',
    "trash": '<path d="M5 7h14M10 7V4h4v3M7 7l1 13h8l1-13"/>',
    "arrow-up": '<path d="M12 19V5M6 11l6-6 6 6"/>',
    "arrow-down": '<path d="M12 5v14M6 13l6 6 6-6"/>',
    "arrow-right": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "settings": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.6 1.6 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1'
                'a1.6 1.6 0 0 0-1.8-.3 1.6 1.6 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.6 1.6 0 0 0-1-1.5 1.6 1.6 0 0 0-1.8'
                '.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.6 1.6 0 0 0 .3-1.8 1.6 1.6 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.6 1.6 '
                '0 0 0 1.5-1 1.6 1.6 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.6 1.6 0 0 0 1.8.3H9a1.6 1.6 0 0 0 '
                '1-1.5V3a2 2 0 1 1 4 0v.1a1.6 1.6 0 0 0 1 1.5 1.6 1.6 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.6 '
                '1.6 0 0 0-.3 1.8V9a1.6 1.6 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.6 1.6 0 0 0-1.5 1z"/>',
    "logout": '<path d="M15 4h4v16h-4"/><path d="M10 8l-4 4 4 4M6 12h10"/>',
    "feed": '<path d="M4 11a9 9 0 0 1 9 9M4 4a16 16 0 0 1 16 16"/><circle cx="5" cy="19" r="1"/>',
}


@register.simple_tag(takes_context=True)
def jsonld_website(context):
    from django.conf import settings
    from django.urls import reverse

    return jsonld({
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": settings.SITE_NAME,
        "url": settings.SITE_URL + "/",
        "potentialAction": {
            "@type": "SearchAction",
            "target": settings.SITE_URL + reverse("search") + "?q={search_term_string}",
            "query-input": "required name=search_term_string",
        },
    })


def _abs(path):
    from django.conf import settings

    return settings.SITE_URL + path


@register.simple_tag
def work_jsonld(work):
    data = {
        "@context": "https://schema.org",
        "@type": "Book",
        "name": work.title,
        "url": _abs(work.get_absolute_url()),
        "description": work.summary,
        "author": {"@type": "Person", "name": work.author.name, "url": _abs(work.author.get_absolute_url())},
        "genre": [t.name for t in work.topics.all()],
    }
    if work.original_language:
        data["inLanguage"] = work.original_language
    if work.year and work.year > 0:
        data["datePublished"] = str(work.year)
    if work.pages:
        data["numberOfPages"] = work.pages
    if work.rating_count:
        data["aggregateRating"] = {
            "@type": "AggregateRating",
            "ratingValue": work.rating_avg_5,
            "bestRating": 5,
            "worstRating": 0.5,
            "ratingCount": work.rating_count,
        }
    return jsonld(data)


@register.simple_tag
def thinker_jsonld(thinker):
    data = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": thinker.name,
        "url": _abs(thinker.get_absolute_url()),
        "description": thinker.tagline,
    }
    if thinker.birthplace:
        data["birthPlace"] = thinker.birthplace
    if thinker.birth_year and thinker.birth_year > 0 and not thinker.years_approx:
        data["birthDate"] = str(thinker.birth_year)
    if thinker.death_year and thinker.death_year > 0 and not thinker.years_approx:
        data["deathDate"] = str(thinker.death_year)
    return jsonld(data)


@register.simple_tag
def review_jsonld(entry):
    data = {
        "@context": "https://schema.org",
        "@type": "Review",
        "url": _abs(entry.get_absolute_url()),
        "author": {"@type": "Person", "name": entry.user.name},
        "datePublished": entry.created_at.date().isoformat(),
        "reviewBody": entry.review[:5000],
        "itemReviewed": {
            "@type": "Book",
            "name": entry.work.title,
            "author": {"@type": "Person", "name": entry.work.author.name},
            "url": _abs(entry.work.get_absolute_url()),
        },
    }
    if entry.rating:
        data["reviewRating"] = {"@type": "Rating", "ratingValue": entry.rating / 2, "bestRating": 5, "worstRating": 0.5}
    return jsonld(data)
