from django.core.paginator import Paginator
from django.db.models import Count, F, Q
from django.shortcuts import get_object_or_404, render

from social.models import Entry, Follow, ReadingList, UserWork

from .models import Era, Quote, School, Thinker, Topic, Work

WORK_SORTS = {
    "popular": ("Most read", ["-read_count", "-featured", "year"]),
    "rating": ("Highest rated", [F("rating_avg").desc(nulls_last=True), "-rating_count", "year"]),
    "oldest": ("Oldest first", ["year", "title"]),
    "newest": ("Newest first", ["-year", "title"]),
    "title": ("Title A–Z", ["title"]),
    "short": ("Shortest", [F("pages").asc(nulls_last=True), "title"]),
}


def work_list(request):
    works = Work.objects.select_related("author", "era")
    filters = {}

    era = request.GET.get("era")
    if era:
        filters["era"] = get_object_or_404(Era, slug=era)
        works = works.filter(era=filters["era"])
    topic = request.GET.get("topic")
    if topic:
        filters["topic"] = get_object_or_404(Topic, slug=topic)
        works = works.filter(topics=filters["topic"])
    school = request.GET.get("school")
    if school:
        filters["school"] = get_object_or_404(School, slug=school)
        works = works.filter(schools=filters["school"])
    difficulty = request.GET.get("difficulty")
    if difficulty in {"1", "2", "3", "4", "5"}:
        filters["difficulty"] = int(difficulty)
        works = works.filter(difficulty__lte=int(difficulty))
    if request.GET.get("free"):
        filters["free"] = True
        works = works.filter(public_domain=True)

    sort = request.GET.get("sort", "popular")
    if sort not in WORK_SORTS:
        sort = "popular"
    works = works.order_by(*WORK_SORTS[sort][1]).distinct()

    page = Paginator(works, 36).get_page(request.GET.get("page"))
    states = _states_for(request.user, page.object_list)
    return render(request, "catalog/work_list.html", {
        "page": page,
        "filters": filters,
        "sort": sort,
        "sorts": {key: label for key, (label, _) in WORK_SORTS.items()},
        "eras": Era.objects.all(),
        "topics": Topic.objects.all(),
        "schools": School.objects.order_by("name"),
        "states": states,
    })


def _states_for(user, works):
    """Map work_id → UserWork for the current user, to badge covers they've read."""
    if not user.is_authenticated:
        return {}
    ids = [w.pk for w in works]
    return {uw.work_id: uw for uw in UserWork.objects.filter(user=user, work_id__in=ids)}


def work_detail(request, slug):
    work = get_object_or_404(Work.objects.select_related("author", "era"), slug=slug)
    entries = Entry.objects.filter(work=work).exclude(review="").select_related("user")

    histogram = {i: 0 for i in range(1, 11)}
    for row in UserWork.objects.filter(work=work, rating__isnull=False).values("rating").annotate(n=Count("id")):
        histogram[row["rating"]] = row["n"]
    hist_max = max(histogram.values()) or 1

    ctx = {
        "work": work,
        "popular_reviews": entries.order_by("-like_count", "-created_at")[:6],
        "recent_reviews": entries.order_by("-created_at")[:6],
        "histogram": [(i, n, round(100 * n / hist_max)) for i, n in histogram.items()],
        "quotes": work.quotes.select_related("thinker")[:4],
        "more_by_author": work.author.works.exclude(pk=work.pk).order_by("year")[:6],
        "similar": _similar_works(work),
        "in_lists": ReadingList.objects.filter(items__work=work).select_related("user")
        .annotate(n=Count("items", distinct=True)).order_by("-is_editorial", "-like_count")[:4],
        "topics": work.topics.all(),
        "schools": work.schools.all(),
    }
    if request.user.is_authenticated:
        ctx["state"] = UserWork.objects.filter(user=request.user, work=work).first()
        ctx["my_lists"] = request.user.reading_lists.annotate(
            has_work=Count("items", filter=Q(items__work=work))
        ).order_by("-updated_at")
        followed = Follow.objects.filter(follower=request.user).values("followed")
        ctx["friends"] = (
            UserWork.objects.filter(work=work, user__in=followed)
            .filter(Q(is_read=True) | Q(rating__isnull=False))
            .select_related("user")[:12]
        )
    return render(request, "catalog/work_detail.html", ctx)


def _similar_works(work, limit=6):
    topic_ids = list(work.topics.values_list("id", flat=True))
    return (
        Work.objects.filter(topics__in=topic_ids)
        .exclude(pk=work.pk)
        .exclude(author=work.author)
        .annotate(shared=Count("topics", filter=Q(topics__in=topic_ids)))
        .select_related("author")
        .order_by("-shared", "-read_count", "-featured")[:limit]
    )


def work_reviews(request, slug):
    work = get_object_or_404(Work.objects.select_related("author"), slug=slug)
    sort = request.GET.get("sort", "popular")
    entries = Entry.objects.filter(work=work).exclude(review="").select_related("user")
    entries = entries.order_by("-created_at") if sort == "recent" else entries.order_by("-like_count", "-created_at")
    page = Paginator(entries, 20).get_page(request.GET.get("page"))
    return render(request, "catalog/work_reviews.html", {"work": work, "page": page, "sort": sort})


def thinker_list(request):
    thinkers = Thinker.objects.select_related("era").annotate(n_works=Count("works"))
    era = request.GET.get("era")
    selected_era = None
    if era:
        selected_era = get_object_or_404(Era, slug=era)
        thinkers = thinkers.filter(era=selected_era)
    sort = request.GET.get("sort", "chronological")
    if sort == "name":
        thinkers = thinkers.order_by("name")
    else:
        sort = "chronological"
        thinkers = thinkers.order_by("birth_year", "name")
    return render(request, "catalog/thinker_list.html", {
        "thinkers": thinkers, "eras": Era.objects.all(), "selected_era": selected_era, "sort": sort,
    })


def thinker_detail(request, slug):
    thinker = get_object_or_404(Thinker.objects.select_related("era"), slug=slug)
    works = thinker.works.order_by("year")
    return render(request, "catalog/thinker_detail.html", {
        "thinker": thinker,
        "works": works,
        "influences": thinker.influences.select_related("era").order_by("birth_year"),
        "influenced": thinker.influenced.select_related("era").order_by("birth_year"),
        "quotes": thinker.quotes.select_related("work"),
        "schools": thinker.schools.all(),
        "topics": thinker.topics.all(),
        "states": _states_for(request.user, works),
        "readers": UserWork.objects.filter(work__author=thinker, is_read=True).values("user").distinct().count(),
    })


def school_list(request):
    eras = Era.objects.prefetch_related("schools")
    return render(request, "catalog/school_list.html", {"eras": eras})


def school_detail(request, slug):
    school = get_object_or_404(School.objects.select_related("era"), slug=slug)
    return render(request, "catalog/school_detail.html", {
        "school": school,
        "thinkers": school.thinkers.select_related("era").order_by("birth_year"),
        "works": school.works.select_related("author").order_by("year"),
    })


def topic_list(request):
    topics = Topic.objects.annotate(
        n_works=Count("works", distinct=True), n_thinkers=Count("thinkers", distinct=True)
    ).order_by("name")
    return render(request, "catalog/topic_list.html", {"topics": topics})


def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    return render(request, "catalog/topic_detail.html", {
        "topic": topic,
        "works": topic.works.select_related("author").order_by("-read_count", "-featured", "year"),
        "thinkers": topic.thinkers.select_related("era").order_by("birth_year"),
    })


def era_detail(request, slug):
    era = get_object_or_404(Era, slug=slug)
    return render(request, "catalog/era_detail.html", {
        "era": era,
        "thinkers": era.thinkers.order_by("birth_year"),
        "works": era.works.select_related("author").order_by("-featured", "-read_count", "year")[:24],
        "schools": era.schools.all(),
        "prev_era": Era.objects.filter(order__lt=era.order).order_by("-order").first(),
        "next_era": Era.objects.filter(order__gt=era.order).order_by("order").first(),
    })


def timeline(request):
    eras = list(Era.objects.all())
    thinkers = list(Thinker.objects.select_related("era").order_by("birth_year", "name"))
    by_era = {era.pk: [] for era in eras}
    for t in thinkers:
        if t.era_id in by_era:
            by_era[t.era_id].append(t)
    return render(request, "catalog/timeline.html", {
        "eras": [(era, by_era[era.pk]) for era in eras],
        "count": len(thinkers),
    })


def quote_list(request):
    quotes = Quote.objects.select_related("thinker", "work").order_by("thinker__birth_year", "id")
    return render(request, "catalog/quote_list.html", {"quotes": quotes})


def quote_detail(request, pk):
    quote = get_object_or_404(Quote.objects.select_related("thinker", "work"), pk=pk)
    more = quote.thinker.quotes.exclude(pk=quote.pk)[:4]
    return render(request, "catalog/quote_detail.html", {"quote": quote, "more": more})
