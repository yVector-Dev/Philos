from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from catalog.models import Era, Quote, School, Thinker, Topic, Work
from social.models import Entry, ReadingList


class SiteSitemap(Sitemap):
    """Always generate absolute URLs on the configured public domain."""

    def get_protocol(self, protocol=None):
        return "https" if settings.SITE_URL.startswith("https") else "http"

    def get_domain(self, site=None):
        return settings.SITE_URL.split("://", 1)[-1]


class StaticSitemap(SiteSitemap):
    priority = 0.8
    changefreq = "daily"

    def items(self):
        return ["home", "work_list", "thinker_list", "school_list", "topic_list", "timeline", "quote_list",
                "list_index", "about"]

    def location(self, item):
        return reverse(item)


class WorkSitemap(SiteSitemap):
    priority = 0.9
    changefreq = "weekly"

    def items(self):
        return Work.objects.order_by("id")

    def lastmod(self, obj):
        return obj.updated_at


class ThinkerSitemap(SiteSitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return Thinker.objects.order_by("id")


class TaxonomySitemap(SiteSitemap):
    priority = 0.6
    changefreq = "weekly"

    def items(self):
        return list(Era.objects.all()) + list(School.objects.all()) + list(Topic.objects.all())


class QuoteSitemap(SiteSitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return Quote.objects.order_by("id")


class ListSitemap(SiteSitemap):
    priority = 0.6
    changefreq = "weekly"

    def items(self):
        return ReadingList.objects.filter(items__isnull=False).distinct().select_related("user").order_by("id")

    def lastmod(self, obj):
        return obj.updated_at


class ReviewSitemap(SiteSitemap):
    priority = 0.4
    changefreq = "monthly"
    limit = 5000

    def items(self):
        return Entry.objects.exclude(review="").select_related("user").order_by("-id")

    def lastmod(self, obj):
        return obj.updated_at


sitemaps = {
    "static": StaticSitemap,
    "works": WorkSitemap,
    "thinkers": ThinkerSitemap,
    "taxonomy": TaxonomySitemap,
    "quotes": QuoteSitemap,
    "lists": ListSitemap,
    "reviews": ReviewSitemap,
}
