"""Populate a LOCAL database with demo members, ratings, reviews, follows and lists.

For development and screenshots only: it refuses to run with DEBUG off unless --force is given.
Demo accounts are prefixed with "demo_" and can be removed with --clear.
"""

import random
from datetime import timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from catalog.models import Work
from social.models import Comment, Entry, EntryLike, Follow, ListItem, ReadingList, UserWork

DEMO_USERS = [
    ("demo_ana", "Ana", "Reading my way from the Presocratics to the present. Mostly Stoics, lots of tea."),
    ("demo_kenji", "Kenji", "Zen, Kyoto School and long walks. Slowly working through the Shōbōgenzō."),
    ("demo_amara", "Amara", "Political theory nerd. Arendt, Fanon, Du Bois. Always arguing about Rawls."),
    ("demo_lucas", "Lucas", "History teacher. Herodotus is the GOAT."),
    ("demo_mira", "Mira", "Existentialist in recovery. Camus over Sartre, fight me."),
    ("demo_omar", "Omar", "Ibn Khaldun, Averroes and the golden age of Baghdad."),
]

REVIEW_SNIPPETS = [
    "I expected to be bored and instead I was underlining every other page. The argument is cleaner than its "
    "reputation, and the parts that feel dated are still worth wrestling with.",
    "Re-reading this ten years later is a completely different experience. What once seemed like abstract "
    "theorising now reads as practical advice for getting through a hard week.",
    "Dense, occasionally maddening, but there are passages here that rearranged how I think. Read it slowly, with "
    "a pencil, and argue back in the margins.",
    "The perfect length for a weekend. I came away with three ideas I keep returning to, which is more than most "
    "books manage.",
    "I disagree with almost everything in it, and that's exactly why everyone should read it once. Steel-man first, "
    "then reply.",
    "Short, sharp and still provocative. Pair it with a modern critic and see who wins.",
]


class Command(BaseCommand):
    help = "Create demo members and activity for local development (never run in production)."

    def add_arguments(self, parser):
        parser.add_argument("--force", action="store_true", help="Run even when DEBUG is off.")
        parser.add_argument("--clear", action="store_true", help="Delete all demo_* accounts and their data.")

    def handle(self, *args, **options):
        if not settings.DEBUG and not options["force"]:
            raise CommandError("seed_demo is for local development. Use --force if you really mean it.")
        User = get_user_model()
        if options["clear"]:
            n, _ = User.objects.filter(username__startswith="demo_").delete()
            self.stdout.write(self.style.SUCCESS(f"Removed demo data ({n} rows)."))
            return

        rng = random.Random(42)
        works = list(Work.objects.order_by("-featured", "id"))
        if not works:
            raise CommandError("Run seed_catalog first.")
        now = timezone.now()
        users = []
        for username, name, bio in DEMO_USERS:
            user, created = User.objects.get_or_create(
                username=username, defaults={"display_name": name, "bio": bio, "email": f"{username}@example.com"}
            )
            if created:
                user.set_unusable_password()
                user.save()
            users.append(user)

        for user in users:
            picks = rng.sample(works[:70], 22)
            for i, work in enumerate(picks):
                rating = rng.choice([6, 7, 7, 8, 8, 8, 9, 9, 10, 10, 5])
                UserWork.objects.update_or_create(
                    user=user, work=work,
                    defaults=dict(is_read=True, rating=rating, is_liked=rating >= 9),
                )
                when = now - timedelta(days=rng.randint(0, 120), hours=rng.randint(0, 23))
                review = rng.choice(REVIEW_SNIPPETS) if i < 4 else ""
                entry = Entry.objects.create(
                    user=user, work=work, rating=rating, review=review, read_on=when.date(), liked=rating >= 9,
                )
                Entry.objects.filter(pk=entry.pk).update(created_at=when)
            for work in rng.sample(works[70:], 5):
                UserWork.objects.get_or_create(user=user, work=work, defaults=dict(want_to_read=True))

        for user in users:
            for other in rng.sample([u for u in users if u != user], 3):
                Follow.objects.get_or_create(follower=user, followed=other)

        reviews = list(Entry.objects.filter(user__in=users).exclude(review=""))
        for entry in reviews:
            for liker in rng.sample(users, rng.randint(0, 4)):
                if liker != entry.user:
                    EntryLike.objects.get_or_create(user=liker, entry=entry)
        for entry in rng.sample(reviews, min(6, len(reviews))):
            commenter = rng.choice([u for u in users if u != entry.user])
            Comment.objects.get_or_create(
                user=commenter, entry=entry, defaults={"body": "Great review — this convinced me to move it up my list."}
            )

        rl, _ = ReadingList.objects.get_or_create(
            user=users[0], slug="desert-island-philosophy",
            defaults=dict(title="Desert Island Philosophy", description="If I could only take ten books.",
                          is_ranked=True),
        )
        if not rl.items.exists():
            for i, work in enumerate(rng.sample(works[:40], 10)):
                ListItem.objects.create(reading_list=rl, work=work, position=i)

        self.stdout.write(self.style.SUCCESS(f"Demo data ready for {len(users)} members."))
