from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    display_name = models.CharField(max_length=60, blank=True)
    bio = models.TextField(max_length=600, blank=True)
    location = models.CharField(max_length=80, blank=True)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username

    @property
    def name(self):
        return self.display_name or self.username

    @property
    def initials(self):
        parts = self.name.split()
        letters = "".join(p[0] for p in parts[:2]) if parts else self.username[:2]
        return letters.upper()

    @property
    def avatar_hue(self):
        # Stable, pleasant colour per user without storing uploads.
        return sum(ord(c) for c in self.username) * 37 % 360

    def get_absolute_url(self):
        return reverse("profile", args=[self.username])


class FavoriteWork(models.Model):
    """Up to four works a user pins to the top of their profile."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorite_links")
    work = models.ForeignKey("catalog.Work", on_delete=models.CASCADE, related_name="+")
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["position"]
        constraints = [
            models.UniqueConstraint(fields=["user", "work"], name="unique_favorite_work"),
        ]

    def __str__(self):
        return f"{self.user} ♥ {self.work}"
