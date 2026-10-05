from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

RATING_VALIDATORS = [MinValueValidator(1), MaxValueValidator(10)]


class UserWork(models.Model):
    """A user's standing relationship with a work: read, liked, want to read, rating.

    Ratings are stored as half-stars on a 1–10 scale (7 = ★★★½).
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="work_states")
    work = models.ForeignKey("catalog.Work", on_delete=models.CASCADE, related_name="user_states")
    is_read = models.BooleanField(default=False)
    is_liked = models.BooleanField(default=False)
    want_to_read = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(null=True, blank=True, validators=RATING_VALIDATORS)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "work"], name="unique_user_work")]
        indexes = [models.Index(fields=["user", "-updated_at"])]

    def __str__(self):
        return f"{self.user} / {self.work}"

    @property
    def is_empty(self):
        return not (self.is_read or self.is_liked or self.want_to_read or self.rating)


class Entry(models.Model):
    """A diary entry: one reading of a work, optionally with a rating and review."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="entries")
    work = models.ForeignKey("catalog.Work", on_delete=models.CASCADE, related_name="entries")
    rating = models.PositiveSmallIntegerField(null=True, blank=True, validators=RATING_VALIDATORS)
    review = models.TextField(blank=True, max_length=12000)
    read_on = models.DateField(null=True, blank=True)
    reread = models.BooleanField(default=False)
    liked = models.BooleanField(default=False)
    like_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "entries"
        indexes = [
            models.Index(fields=["-created_at"]),
            models.Index(fields=["work", "-like_count"]),
        ]

    def __str__(self):
        return f"{self.user} read {self.work}"

    def get_absolute_url(self):
        return reverse("review_detail", args=[self.user.username, self.pk])

    @property
    def has_review(self):
        return bool(self.review.strip())

    def refresh_counts(self):
        self.like_count = self.likes.count()
        self.comment_count = self.comments.count()
        Entry.objects.filter(pk=self.pk).update(like_count=self.like_count, comment_count=self.comment_count)


class EntryLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="entry_likes")
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "entry"], name="unique_entry_like")]


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.user} on {self.entry_id}"


class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following_links")
    followed = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="follower_links")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["follower", "followed"], name="unique_follow"),
            models.CheckConstraint(condition=~models.Q(follower=models.F("followed")), name="no_self_follow"),
        ]

    def __str__(self):
        return f"{self.follower} → {self.followed}"


class ReadingList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reading_lists")
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=160)
    description = models.TextField(blank=True, max_length=4000)
    is_ranked = models.BooleanField(default=False)
    is_editorial = models.BooleanField(default=False, help_text="Curated by Philos editors; featured on the home page.")
    like_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        constraints = [models.UniqueConstraint(fields=["user", "slug"], name="unique_list_slug_per_user")]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("list_detail", args=[self.user.username, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:140] or "list"
            slug, n = base, 2
            while ReadingList.objects.filter(user=self.user, slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def refresh_counts(self):
        self.like_count = self.likes.count()
        ReadingList.objects.filter(pk=self.pk).update(like_count=self.like_count)


class ListItem(models.Model):
    reading_list = models.ForeignKey(ReadingList, on_delete=models.CASCADE, related_name="items")
    work = models.ForeignKey("catalog.Work", on_delete=models.CASCADE, related_name="list_items")
    position = models.PositiveIntegerField(default=0)
    note = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ["position", "id"]
        constraints = [models.UniqueConstraint(fields=["reading_list", "work"], name="unique_list_work")]


class ListLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="list_likes")
    reading_list = models.ForeignKey(ReadingList, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "reading_list"], name="unique_list_like")]
