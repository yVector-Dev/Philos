from datetime import timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.cache import cache_control

from catalog.models import Era, Quote, School, Thinker, Topic, Work
from social.models import Entry, Follow, ReadingList, UserWork

User = get_user_model()


def quote_of_the_day():
    count = Quote.objects.count()
    if not count:
        return None
    index = timezone.localdate().toordinal() % count
    return Quote.objects.select_related("thinker", "work").order_by("id")[index]


def popular_this_week(limit=12):
    week_ago = timezone.now() - timedelta(days=7)
    return (
        Work.objects.select_related("author")
        .annotate(
            recent=Count("user_states", filter=Q(user_states__updated_at__gte=week_ago), distinct=True)
            + Count("entries", filter=Q(entries__created_at__gte=week_ago), distinct=True)
        )
        .order_by("-recent", "-read_count", "-featured", "year")[:limit]
    )


def home(request):
    reviews = Entry.objects.exclude(review="").select_related("user", "work", "work__author")
    lists = (
        ReadingList.objects.filter(is_editorial=True)
        .select_related("user")
        .prefetch_related("items__work")
        .annotate(n=Count("items"))
        .order_by("id")
    )
    ctx = {
        "quote": quote_of_the_day(),
        "popular": popular_this_week(),
        "editorial_lists": lists[:6],
        "recent_reviews": reviews.order_by("-created_at")[:6],
        "popular_reviews": reviews.filter(created_at__gte=timezone.now() - timedelta(days=30))
        .order_by("-like_count", "-created_at")[:4],
        "eras": Era.objects.annotate(
            n_thinkers=Count("thinkers", distinct=True), n_works=Count("works", distinct=True)
        ).order_by("order"),
        "topics": Topic.objects.all(),
        "hero_works": Work.objects.filter(featured=True).select_related("author").order_by("?")[:18],
        "counts": {
            "works": Work.objects.count(),
            "thinkers": Thinker.objects.count(),
            "members": User.objects.count(),
            "reviews": Entry.objects.exclude(review="").count(),
        },
    }
    if request.user.is_authenticated:
        followed = Follow.objects.filter(follower=request.user).values("followed")
        ctx["friends_activity"] = (
            Entry.objects.filter(user__in=followed).select_related("user", "work", "work__author")
            .order_by("-created_at")[:12]
        )
        ctx["to_read"] = (
            UserWork.objects.filter(user=request.user, want_to_read=True)
            .select_related("work", "work__author").order_by("-updated_at")[:6]
        )
    return render(request, "core/home.html", ctx)


@login_required
def welcome(request):
    """Onboarding: mark a handful of works you've already read, then follow people."""
    works = Work.objects.filter(featured=True).select_related("author").order_by("year")
    states = {
        s.work_id: s for s in UserWork.objects.filter(user=request.user, work__in=works)
    }
    return render(request, "core/welcome.html", {
        "works": works,
        "states": states,
        "lists": ReadingList.objects.filter(is_editorial=True).order_by("id")[:3],
    })


def search(request):
    q = request.GET.get("q", "").strip()[:100]
    ctx = {"q": q}
    if q:
        ctx.update({
            "works": Work.objects.filter(
                Q(title__icontains=q) | Q(original_title__icontains=q) | Q(author__name__icontains=q)
            ).select_related("author").order_by("-read_count", "-featured", "year")[:24],
            "thinkers": Thinker.objects.filter(Q(name__icontains=q) | Q(tagline__icontains=q))[:12],
            "schools": School.objects.filter(name__icontains=q)[:6],
            "lists": ReadingList.objects.filter(title__icontains=q).select_related("user")[:8],
            "members": User.objects.filter(Q(username__icontains=q) | Q(display_name__icontains=q))[:8],
            "quotes": Quote.objects.filter(text__icontains=q).select_related("thinker")[:6],
        })
        ctx["total"] = sum(len(ctx[k]) for k in ("works", "thinkers", "schools", "lists", "members", "quotes"))
    return render(request, "core/search.html", ctx)


def about(request):
    return render(request, "core/about.html", {
        "counts": {"works": Work.objects.count(), "thinkers": Thinker.objects.count()},
    })


@cache_control(max_age=86400, public=True)
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /accounts/",
        "Disallow: /settings/",
        "Disallow: /admin/",
        "Disallow: /activity/",
        "Disallow: /search/",
        "Allow: /",
        "",
        f"Sitemap: {settings.SITE_URL}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines) + "\n", content_type="text/plain")


def page_not_found(request, exception):
    return render(request, "404.html", status=404)
