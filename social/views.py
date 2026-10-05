from datetime import date
from itertools import groupby

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count, Max, Q
from django.http import Http404, HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from catalog.models import Era, Work

from .forms import CommentForm, EntryForm, ReadingListForm
from .models import Comment, Entry, EntryLike, Follow, ListItem, ListLike, ReadingList, UserWork

User = get_user_model()


def _is_ajax(request):
    return request.headers.get("x-requested-with") == "XMLHttpRequest"


def _back(request, fallback):
    target = request.POST.get("next") or request.META.get("HTTP_REFERER")
    if target and url_has_allowed_host_and_scheme(
        target, allowed_hosts={request.get_host()}, require_https=request.is_secure()
    ):
        return redirect(target)
    return redirect(fallback)


def _work_payload(work, state):
    work.refresh_from_db(fields=["rating_avg", "rating_count", "read_count", "like_count", "want_count"])
    return {
        "is_read": bool(state and state.is_read),
        "is_liked": bool(state and state.is_liked),
        "want_to_read": bool(state and state.want_to_read),
        "rating": state.rating if state else None,
        "stats": {
            "read_count": work.read_count,
            "like_count": work.like_count,
            "rating_count": work.rating_count,
            "rating_avg_5": work.rating_avg_5,
        },
    }


# ── Reading state ────────────────────────────────────────────────────────────


@login_required
@require_POST
def work_status(request, slug):
    work = get_object_or_404(Work, slug=slug)
    state, _ = UserWork.objects.get_or_create(user=request.user, work=work)
    action = request.POST.get("action")

    if action == "read":
        state.is_read = not state.is_read
        if state.is_read:
            state.want_to_read = False
        else:
            state.rating = None
            state.is_liked = False
    elif action == "like":
        state.is_liked = not state.is_liked
        if state.is_liked:
            state.is_read = True
            state.want_to_read = False
    elif action == "want":
        state.want_to_read = not state.want_to_read
    elif action == "rate":
        try:
            rating = int(request.POST.get("rating", 0))
        except ValueError:
            rating = 0
        if 1 <= rating <= 10:
            state.rating = rating
            state.is_read = True
            state.want_to_read = False
        else:
            state.rating = None
    else:
        return JsonResponse({"error": "Unknown action"}, status=400)

    if state.is_empty:
        state.delete()
        state = None
    else:
        state.save()

    if _is_ajax(request):
        return JsonResponse(_work_payload(work, state))
    return _back(request, work.get_absolute_url())


@login_required
def log_work(request, slug):
    work = get_object_or_404(Work.objects.select_related("author"), slug=slug)
    state = UserWork.objects.filter(user=request.user, work=work).first()
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            entry = Entry.objects.create(
                user=request.user, work=work, rating=data["rating"], review=data["review"].strip(),
                read_on=data["read_on"], reread=data["reread"], liked=data["liked"],
            )
            state = state or UserWork(user=request.user, work=work)
            state.is_read = True
            state.want_to_read = False
            if data["rating"]:
                state.rating = data["rating"]
            if data["liked"]:
                state.is_liked = True
            state.save()
            if entry.has_review:
                messages.success(request, "Your review is published.")
                return redirect(entry.get_absolute_url())
            messages.success(request, f"Logged “{work.title}” to your diary.")
            return redirect(work.get_absolute_url())
    else:
        form = EntryForm(initial={
            "rating": state.rating if state else None,
            "liked": bool(state and state.is_liked),
            "read_on": timezone.localdate(),
            "reread": bool(state and state.is_read),
        })
    return render(request, "social/log_form.html", {"work": work, "form": form, "state": state})


# ── Reviews ──────────────────────────────────────────────────────────────────


def _get_entry(username, pk):
    entry = get_object_or_404(Entry.objects.select_related("user", "work", "work__author"), pk=pk)
    if entry.user.username != username:
        raise Http404
    return entry


def review_detail(request, username, pk):
    entry = _get_entry(username, pk)
    ctx = {
        "entry": entry,
        "comments": entry.comments.select_related("user"),
        "comment_form": CommentForm(),
        "liked": request.user.is_authenticated and entry.likes.filter(user=request.user).exists(),
        "more_reviews": Entry.objects.filter(work=entry.work).exclude(review="").exclude(pk=entry.pk)
        .select_related("user").order_by("-like_count", "-created_at")[:3],
    }
    return render(request, "social/review_detail.html", ctx)


@login_required
def review_edit(request, username, pk):
    entry = _get_entry(username, pk)
    if entry.user != request.user:
        return HttpResponseForbidden()
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            entry.rating = data["rating"]
            entry.review = data["review"].strip()
            entry.read_on = data["read_on"]
            entry.reread = data["reread"]
            entry.liked = data["liked"]
            entry.save()
            if data["rating"]:
                UserWork.objects.update_or_create(
                    user=request.user, work=entry.work, defaults={"rating": data["rating"], "is_read": True}
                )
            messages.success(request, "Entry updated.")
            return redirect(entry.get_absolute_url())
    else:
        form = EntryForm(initial={
            "rating": entry.rating, "review": entry.review, "read_on": entry.read_on,
            "reread": entry.reread, "liked": entry.liked,
        })
    return render(request, "social/log_form.html", {"work": entry.work, "form": form, "entry": entry})


@login_required
@require_POST
def review_delete(request, username, pk):
    entry = _get_entry(username, pk)
    if entry.user != request.user:
        return HttpResponseForbidden()
    work = entry.work
    entry.delete()
    messages.success(request, "Entry deleted.")
    return redirect(work.get_absolute_url())


@login_required
@require_POST
def review_like(request, username, pk):
    entry = _get_entry(username, pk)
    like = EntryLike.objects.filter(user=request.user, entry=entry).first()
    if like:
        like.delete()
        liked = False
    else:
        EntryLike.objects.create(user=request.user, entry=entry)
        liked = True
    entry.refresh_from_db(fields=["like_count"])
    if _is_ajax(request):
        return JsonResponse({"liked": liked, "count": entry.like_count})
    return _back(request, entry.get_absolute_url())


@login_required
@require_POST
def comment_create(request, username, pk):
    entry = _get_entry(username, pk)
    form = CommentForm(request.POST)
    if form.is_valid() and form.cleaned_data["body"].strip():
        Comment.objects.create(user=request.user, entry=entry, body=form.cleaned_data["body"].strip())
    return redirect(entry.get_absolute_url() + "#comments")


@login_required
@require_POST
def comment_delete(request, pk):
    comment = get_object_or_404(Comment.objects.select_related("entry", "entry__user"), pk=pk)
    if request.user not in (comment.user, comment.entry.user):
        return HttpResponseForbidden()
    entry = comment.entry
    comment.delete()
    return redirect(entry.get_absolute_url() + "#comments")


# ── Profiles ─────────────────────────────────────────────────────────────────


def _profile_context(request, username, tab):
    profile_user = get_object_or_404(User, username=username)
    this_year = timezone.localdate().year
    stats = {
        "read": UserWork.objects.filter(user=profile_user, is_read=True).count(),
        "this_year": Entry.objects.filter(user=profile_user)
        .filter(Q(read_on__year=this_year) | Q(read_on__isnull=True, created_at__year=this_year))
        .values("work").distinct().count(),
        "reviews": Entry.objects.filter(user=profile_user).exclude(review="").count(),
        "lists": profile_user.reading_lists.count(),
        "following": profile_user.following_links.count(),
        "followers": profile_user.follower_links.count(),
    }
    is_following = (
        request.user.is_authenticated
        and request.user != profile_user
        and Follow.objects.filter(follower=request.user, followed=profile_user).exists()
    )
    return {"profile_user": profile_user, "stats": stats, "is_following": is_following, "tab": tab}


def profile(request, username):
    ctx = _profile_context(request, username, "profile")
    u = ctx["profile_user"]
    read_states = UserWork.objects.filter(user=u, is_read=True)
    eras = Era.objects.annotate(
        n=Count("works__user_states", filter=Q(works__user_states__user=u, works__user_states__is_read=True))
    ).order_by("order")
    era_max = max([e.n for e in eras] or [0]) or 1
    ratings = {i: 0 for i in range(1, 11)}
    for row in read_states.filter(rating__isnull=False).values("rating").annotate(n=Count("id")):
        ratings[row["rating"]] = row["n"]
    rating_max = max(ratings.values()) or 1
    ctx.update({
        "favorites": [f.work for f in u.favorite_links.select_related("work", "work__author")],
        "recent": read_states.select_related("work", "work__author").order_by("-updated_at")[:8],
        "recent_reviews": Entry.objects.filter(user=u).exclude(review="").select_related("work", "work__author")[:3],
        "lists": u.reading_lists.prefetch_related("items__work")[:3],
        "era_breakdown": [(e, e.n, round(100 * e.n / era_max)) for e in eras],
        "eras_explored": sum(1 for e in eras if e.n),
        "rating_spread": [(i, n, round(100 * n / rating_max)) for i, n in ratings.items()],
    })
    return render(request, "social/profile.html", ctx)


def profile_diary(request, username):
    ctx = _profile_context(request, username, "diary")
    entries = Entry.objects.filter(user=ctx["profile_user"]).select_related("work", "work__author")
    entries = entries.order_by("-read_on", "-created_at")
    page = Paginator(entries, 50).get_page(request.GET.get("page"))

    def month_key(e):
        d = e.read_on or timezone.localdate(e.created_at)
        return date(d.year, d.month, 1)

    ctx["page"] = page
    ctx["months"] = [(month, list(items)) for month, items in groupby(page.object_list, key=month_key)]
    return render(request, "social/profile_diary.html", ctx)


def profile_reviews(request, username):
    ctx = _profile_context(request, username, "reviews")
    entries = Entry.objects.filter(user=ctx["profile_user"]).exclude(review="").select_related("work", "work__author")
    ctx["page"] = Paginator(entries, 20).get_page(request.GET.get("page"))
    return render(request, "social/profile_reviews.html", ctx)


def _profile_works(request, username, tab, filter_kwargs, title, empty):
    ctx = _profile_context(request, username, tab)
    states = UserWork.objects.filter(user=ctx["profile_user"], **filter_kwargs).select_related("work", "work__author")
    sort = request.GET.get("sort", "recent")
    order = {
        "recent": ["-updated_at"],
        "rating": ["-rating", "-updated_at"],
        "year": ["work__year"],
        "title": ["work__title"],
    }.get(sort, ["-updated_at"])
    ctx.update({
        "page": Paginator(states.order_by(*order), 48).get_page(request.GET.get("page")),
        "sort": sort,
        "title": title,
        "empty": empty,
    })
    return render(request, "social/profile_works.html", ctx)


def profile_works(request, username):
    return _profile_works(request, username, "works", {"is_read": True}, "Read", "No works read yet.")


def profile_to_read(request, username):
    return _profile_works(request, username, "to-read", {"want_to_read": True}, "To read",
                          "Nothing on the reading list yet.")


def profile_likes(request, username):
    return _profile_works(request, username, "likes", {"is_liked": True}, "Liked works", "No liked works yet.")


def profile_lists(request, username):
    ctx = _profile_context(request, username, "lists")
    ctx["lists"] = (
        ctx["profile_user"].reading_lists.prefetch_related("items__work").annotate(n=Count("items")).order_by("-updated_at")
    )
    return render(request, "social/profile_lists.html", ctx)


def profile_network(request, username, direction):
    ctx = _profile_context(request, username, direction)
    u = ctx["profile_user"]
    if direction == "following":
        people = User.objects.filter(follower_links__follower=u)
    else:
        people = User.objects.filter(following_links__followed=u)
    ctx["people"] = people.annotate(n_read=Count("work_states", filter=Q(work_states__is_read=True))).order_by("username")
    return render(request, "social/profile_network.html", ctx)


@login_required
@require_POST
def follow_toggle(request, username):
    target = get_object_or_404(User, username=username)
    if target == request.user:
        return redirect(target.get_absolute_url())
    follow = Follow.objects.filter(follower=request.user, followed=target).first()
    if follow:
        follow.delete()
        following = False
    else:
        Follow.objects.create(follower=request.user, followed=target)
        following = True
    if _is_ajax(request):
        return JsonResponse({"following": following, "followers": target.follower_links.count()})
    return _back(request, target.get_absolute_url())


# ── Lists ────────────────────────────────────────────────────────────────────


def list_index(request):
    base = ReadingList.objects.select_related("user").prefetch_related("items__work").annotate(n=Count("items"))
    return render(request, "social/list_index.html", {
        "editorial": base.filter(is_editorial=True).order_by("id"),
        "popular": base.filter(is_editorial=False, n__gt=0).order_by("-like_count", "-updated_at")[:12],
        "recent": base.filter(is_editorial=False, n__gt=0).order_by("-created_at")[:12],
    })


def _get_list(username, slug):
    return get_object_or_404(ReadingList.objects.select_related("user"), user__username=username, slug=slug)


def list_detail(request, username, slug):
    reading_list = _get_list(username, slug)
    items = list(reading_list.items.select_related("work", "work__author", "work__era"))
    read_ids = set()
    if request.user.is_authenticated:
        read_ids = set(
            UserWork.objects.filter(user=request.user, is_read=True, work__in=[i.work for i in items])
            .values_list("work_id", flat=True)
        )
    return render(request, "social/list_detail.html", {
        "reading_list": reading_list,
        "items": items,
        "read_ids": read_ids,
        "read_pct": round(100 * len(read_ids) / len(items)) if items else 0,
        "liked": request.user.is_authenticated and reading_list.likes.filter(user=request.user).exists(),
        "is_owner": request.user == reading_list.user,
    })


@login_required
def list_create(request):
    work = None
    if request.GET.get("add") or request.POST.get("add"):
        work = Work.objects.filter(slug=request.GET.get("add") or request.POST.get("add")).first()
    if request.method == "POST":
        form = ReadingListForm(request.POST)
        if form.is_valid():
            reading_list = form.save(commit=False)
            reading_list.user = request.user
            reading_list.save()
            if work:
                ListItem.objects.create(reading_list=reading_list, work=work, position=0)
            messages.success(request, "List created. Add works from any work page.")
            return redirect(reading_list.get_absolute_url())
    else:
        form = ReadingListForm()
    return render(request, "social/list_form.html", {"form": form, "work": work})


@login_required
def list_edit(request, username, slug):
    reading_list = _get_list(username, slug)
    if reading_list.user != request.user:
        return HttpResponseForbidden()
    if request.method == "POST":
        form = ReadingListForm(request.POST, instance=reading_list)
        if form.is_valid():
            form.save()
            messages.success(request, "List saved.")
            return redirect(reading_list.get_absolute_url())
    else:
        form = ReadingListForm(instance=reading_list)
    return render(request, "social/list_form.html", {"form": form, "reading_list": reading_list})


@login_required
@require_POST
def list_delete(request, username, slug):
    reading_list = _get_list(username, slug)
    if reading_list.user != request.user:
        return HttpResponseForbidden()
    reading_list.delete()
    messages.success(request, "List deleted.")
    return redirect("profile_lists", username=request.user.username)


@login_required
@require_POST
def list_like(request, username, slug):
    reading_list = _get_list(username, slug)
    like = ListLike.objects.filter(user=request.user, reading_list=reading_list).first()
    if like:
        like.delete()
    else:
        ListLike.objects.create(user=request.user, reading_list=reading_list)
    reading_list.refresh_from_db(fields=["like_count"])
    if _is_ajax(request):
        return JsonResponse({"liked": like is None, "count": reading_list.like_count})
    return _back(request, reading_list.get_absolute_url())


@login_required
@require_POST
def list_toggle_item(request):
    """Add a work to one of the user's lists, or remove it if already there."""
    reading_list = get_object_or_404(ReadingList, pk=request.POST.get("list"), user=request.user)
    work = get_object_or_404(Work, pk=request.POST.get("work"))
    item = ListItem.objects.filter(reading_list=reading_list, work=work).first()
    if item:
        item.delete()
        added = False
    else:
        last = reading_list.items.aggregate(m=Max("position"))["m"]
        ListItem.objects.create(reading_list=reading_list, work=work, position=(last or 0) + 1)
        added = True
    reading_list.save(update_fields=["updated_at"])
    if _is_ajax(request):
        return JsonResponse({"added": added, "list": reading_list.title})
    verb = "Added to" if added else "Removed from"
    messages.success(request, f"{verb} “{reading_list.title}”.")
    return _back(request, work.get_absolute_url())


@login_required
@require_POST
def list_move_item(request, pk):
    item = get_object_or_404(ListItem.objects.select_related("reading_list"), pk=pk, reading_list__user=request.user)
    items = list(item.reading_list.items.all())
    index = items.index(item)
    swap = index - 1 if request.POST.get("direction") == "up" else index + 1
    if 0 <= swap < len(items):
        items[index], items[swap] = items[swap], items[index]
        for position, it in enumerate(items):
            if it.position != position:
                it.position = position
                it.save(update_fields=["position"])
    return redirect(item.reading_list.get_absolute_url())


# ── Discovery ────────────────────────────────────────────────────────────────


def activity(request):
    """What the people you follow have been reading (or everyone, if you follow nobody)."""
    scope = request.GET.get("scope", "following")
    entries = Entry.objects.select_related("user", "work", "work__author")
    lists = ReadingList.objects.select_related("user").prefetch_related("items__work").annotate(n=Count("items"))
    following_count = 0
    if request.user.is_authenticated:
        following_count = request.user.following_links.count()
    if scope == "following" and request.user.is_authenticated and following_count:
        followed = Follow.objects.filter(follower=request.user).values("followed")
        entries = entries.filter(Q(user__in=followed) | Q(user=request.user))
        lists = lists.filter(user__in=followed)
    else:
        scope = "everyone"
    lists = lists.filter(is_editorial=False, n__gt=0)
    items = [("entry", e.created_at, e) for e in entries.order_by("-created_at")[:60]]
    items += [("list", rl.created_at, rl) for rl in lists.order_by("-created_at")[:20]]
    items.sort(key=lambda t: t[1], reverse=True)
    return render(request, "social/activity.html", {
        "items": items[:60], "scope": scope, "following_count": following_count,
        "suggested": _suggested_members(request.user),
    })


def _suggested_members(user, limit=6):
    people = User.objects.annotate(n_entries=Count("entries")).filter(n_entries__gt=0)
    if user.is_authenticated:
        people = people.exclude(pk=user.pk).exclude(follower_links__follower=user)
    return people.order_by("-n_entries")[:limit]


def members(request):
    people = (
        User.objects.annotate(
            n_read=Count("work_states", filter=Q(work_states__is_read=True), distinct=True),
            n_reviews=Count("entries", filter=~Q(entries__review=""), distinct=True),
        )
        .filter(Q(n_read__gt=0) | Q(n_reviews__gt=0))
        .order_by("-n_reviews", "-n_read")
    )
    page = Paginator(people, 30).get_page(request.GET.get("page"))
    return render(request, "social/members.html", {"page": page})
