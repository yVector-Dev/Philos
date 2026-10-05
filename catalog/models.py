import hashlib

from django.db import models
from django.db.models import Avg, Count, Q
from django.urls import reverse


def format_year(year, approx=False):
    """Render a signed year the way readers expect: '399 BCE', 'c. 1200'."""
    if year is None:
        return ""
    prefix = "c. " if approx else ""
    if year < 0:
        return f"{prefix}{-year} BCE"
    if year < 1000:
        return f"{prefix}{year} CE"
    return f"{prefix}{year}"


# Cover colours: deep, bookish tones that read well with light text.
COVER_PALETTE = [
    "#7a2e2e",  # oxblood
    "#1f4e5a",  # deep teal
    "#24365c",  # navy
    "#2f4a34",  # forest
    "#8a5a1f",  # ochre
    "#4f2d4f",  # plum
    "#3d4650",  # slate
    "#9a4b2f",  # terracotta
    "#4d5228",  # olive
    "#33306b",  # indigo
    "#5c3b28",  # walnut
    "#1d3d33",  # pine
]


def _hash(value):
    return int(hashlib.md5(value.encode("utf-8")).hexdigest(), 16)


class Era(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    summary = models.CharField(max_length=280, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    color = models.CharField(max_length=7, default="#3d4650")

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("era_detail", args=[self.slug])

    @property
    def span(self):
        end = format_year(self.end_year) if self.end_year else "present"
        return f"{format_year(self.start_year)} – {end}"


class School(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    era = models.ForeignKey(Era, null=True, blank=True, on_delete=models.SET_NULL, related_name="schools")
    summary = models.CharField(max_length=280, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("school_detail", args=[self.slug])


class Topic(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=280, blank=True)
    question = models.CharField(
        max_length=200, blank=True, help_text="The big question this branch asks, e.g. 'How should I live?'"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("topic_detail", args=[self.slug])


class Thinker(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    years_approx = models.BooleanField(default=False)
    dates_label = models.CharField(
        max_length=80, blank=True, help_text="Overrides the computed lifespan, e.g. 'fl. 6th century BCE'."
    )
    birthplace = models.CharField(max_length=120, blank=True)
    era = models.ForeignKey(Era, null=True, blank=True, on_delete=models.SET_NULL, related_name="thinkers")
    schools = models.ManyToManyField(School, blank=True, related_name="thinkers")
    topics = models.ManyToManyField(Topic, blank=True, related_name="thinkers")
    tagline = models.CharField(max_length=200, blank=True, help_text="One line: who they were.")
    bio = models.TextField(blank=True)
    influences = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="influenced")

    class Meta:
        ordering = ["birth_year", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("thinker_detail", args=[self.slug])

    @property
    def lifespan(self):
        if self.dates_label:
            return self.dates_label
        if self.birth_year is None and self.death_year is None:
            return ""
        born = format_year(self.birth_year, self.years_approx) if self.birth_year is not None else "?"
        if self.death_year is None:
            return f"b. {born}"
        died = format_year(self.death_year, self.years_approx)
        # "c. 470 BCE – c. 399 BCE" reads better as "c. 470 – 399 BCE".
        if self.birth_year is not None and self.birth_year < 0 and self.death_year < 0:
            prefix = "c. " if self.years_approx else ""
            return f"{prefix}{-self.birth_year} – {-self.death_year} BCE"
        return f"{born} – {died}"

    @property
    def initials(self):
        words = [w for w in self.name.replace("-", " ").split() if w[0].isupper()]
        if not words:
            return self.name[:2].upper()
        if len(words) == 1:
            return words[0][:2].upper() if len(words[0]) > 1 else words[0].upper()
        return (words[0][0] + words[-1][0]).upper()

    @property
    def wikipedia_url(self):
        return "https://en.wikipedia.org/wiki/Special:Search?search=" + self.name.replace(" ", "+")


class Work(models.Model):
    KIND_CHOICES = [
        ("book", "Book"),
        ("dialogue", "Dialogue"),
        ("treatise", "Treatise"),
        ("essay", "Essay"),
        ("letters", "Letters"),
        ("aphorisms", "Aphorisms"),
        ("poem", "Poem"),
        ("history", "History"),
        ("novel", "Novel"),
        ("scripture", "Sacred text"),
        ("lectures", "Lectures"),
        ("pamphlet", "Pamphlet"),
    ]
    DIFFICULTY_CHOICES = [
        (1, "Gentle"),
        (2, "Approachable"),
        (3, "Demanding"),
        (4, "Challenging"),
        (5, "Formidable"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Thinker, on_delete=models.CASCADE, related_name="works")
    year = models.IntegerField(null=True, blank=True)
    year_approx = models.BooleanField(default=False)
    era = models.ForeignKey(Era, null=True, blank=True, on_delete=models.SET_NULL, related_name="works")
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default="book")
    original_title = models.CharField(max_length=200, blank=True)
    original_language = models.CharField(max_length=60, blank=True)
    pages = models.PositiveIntegerField(null=True, blank=True, help_text="Typical length in a modern edition.")
    difficulty = models.PositiveSmallIntegerField(choices=DIFFICULTY_CHOICES, default=3)
    summary = models.CharField(max_length=300, help_text="One or two sentences.")
    description = models.TextField(blank=True)
    key_ideas = models.TextField(blank=True, help_text="One idea per line.")
    topics = models.ManyToManyField(Topic, blank=True, related_name="works")
    schools = models.ManyToManyField(School, blank=True, related_name="works")
    public_domain = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    # Denormalised community stats, refreshed whenever a user acts on the work.
    rating_avg = models.FloatField(null=True, blank=True)
    rating_count = models.PositiveIntegerField(default=0)
    read_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)
    want_count = models.PositiveIntegerField(default=0)
    review_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year", "title"]
        indexes = [
            models.Index(fields=["-read_count"]),
            models.Index(fields=["-rating_avg"]),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("work_detail", args=[self.slug])

    @property
    def year_display(self):
        return format_year(self.year, self.year_approx)

    @property
    def key_idea_list(self):
        return [line.strip() for line in self.key_ideas.splitlines() if line.strip()]

    @property
    def cover_color(self):
        return COVER_PALETTE[_hash(self.slug) % len(COVER_PALETTE)]

    @property
    def cover_style(self):
        return ("frame", "band", "ruled")[_hash(self.slug + "style") % 3]

    @property
    def cover_title_class(self):
        longest = max((len(w) for w in self.title.split()), default=0)
        if len(self.title) > 38:
            return "cover-long"
        if longest >= 11:
            return "cover-longword"
        if len(self.title) < 13:
            return "cover-short"
        return ""

    @property
    def rating_avg_5(self):
        """Average on a five-star scale (ratings are stored as half-stars, 1–10)."""
        return round(self.rating_avg / 2, 2) if self.rating_avg is not None else None

    @property
    def free_text_url(self):
        if not self.public_domain:
            return ""
        query = f"{self.title} {self.author.name}".replace(" ", "+")
        return f"https://www.gutenberg.org/ebooks/search/?query={query}"

    def refresh_stats(self):
        from social.models import Entry, UserWork

        agg = UserWork.objects.filter(work=self).aggregate(
            rating_avg=Avg("rating"),
            rating_count=Count("id", filter=Q(rating__isnull=False)),
            read_count=Count("id", filter=Q(is_read=True)),
            like_count=Count("id", filter=Q(is_liked=True)),
            want_count=Count("id", filter=Q(want_to_read=True)),
        )
        agg["review_count"] = Entry.objects.filter(work=self).exclude(review="").count()
        for field, value in agg.items():
            setattr(self, field, value)
        Work.objects.filter(pk=self.pk).update(**agg)


class Quote(models.Model):
    text = models.TextField()
    thinker = models.ForeignKey(Thinker, on_delete=models.CASCADE, related_name="quotes")
    work = models.ForeignKey(Work, null=True, blank=True, on_delete=models.SET_NULL, related_name="quotes")
    source = models.CharField(max_length=200, blank=True, help_text="Where it comes from, if not a catalogued work.")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.thinker}: {self.text[:60]}"

    def get_absolute_url(self):
        return reverse("quote_detail", args=[self.pk])

    @property
    def source_display(self):
        if self.work_id:
            return self.work.title
        return self.source
