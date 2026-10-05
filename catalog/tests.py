from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from catalog.models import Era, Quote, Thinker, Work, format_year
from catalog.seed.quotes_lists import EDITORIAL_LISTS, QUOTES
from catalog.seed.thinkers import THINKERS
from catalog.seed.works_classical import WORKS_CLASSICAL
from catalog.seed.works_modern import WORKS_MODERN


class FormatYearTests(TestCase):
    def test_formats(self):
        self.assertEqual(format_year(-399), "399 BCE")
        self.assertEqual(format_year(-375, approx=True), "c. 375 BCE")
        self.assertEqual(format_year(426), "426 CE")
        self.assertEqual(format_year(1781), "1781")
        self.assertEqual(format_year(None), "")


class SeedDataIntegrityTests(TestCase):
    """The hand-written catalogue must be internally consistent."""

    def test_unique_slugs(self):
        thinker_slugs = [t["slug"] for t in THINKERS]
        work_slugs = [w["slug"] for w in WORKS_CLASSICAL + WORKS_MODERN]
        self.assertEqual(len(thinker_slugs), len(set(thinker_slugs)))
        self.assertEqual(len(work_slugs), len(set(work_slugs)))

    def test_references_resolve(self):
        thinkers = {t["slug"] for t in THINKERS}
        works = {w["slug"] for w in WORKS_CLASSICAL + WORKS_MODERN}
        for t in THINKERS:
            for inf in t["influences"]:
                self.assertIn(inf, thinkers, f"{t['slug']} influence {inf}")
        for w in WORKS_CLASSICAL + WORKS_MODERN:
            self.assertIn(w["author"], thinkers, w["slug"])
            self.assertEqual(len(w["ideas"]), 3, w["slug"])
            self.assertLessEqual(len(w["summary"]), 300, w["slug"])
        for thinker, work, _source, _text in QUOTES:
            self.assertIn(thinker, thinkers)
            if work:
                self.assertIn(work, works)
        for _title, _ranked, _desc, slugs in EDITORIAL_LISTS:
            for slug in slugs:
                self.assertIn(slug, works)


class CatalogViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_catalog", verbosity=0)

    def test_seed_is_idempotent(self):
        before = (Thinker.objects.count(), Work.objects.count(), Quote.objects.count())
        call_command("seed_catalog", verbosity=0)
        self.assertEqual(before, (Thinker.objects.count(), Work.objects.count(), Quote.objects.count()))

    def test_work_era_matches_year(self):
        work = Work.objects.get(slug="critique-of-pure-reason")
        self.assertEqual(work.era.slug, "early-modern")
        self.assertEqual(Work.objects.get(slug="republic").era.slug, "ancient")

    def test_public_pages_render(self):
        work = Work.objects.get(slug="republic")
        era = Era.objects.get(slug="ancient")
        urls = [
            reverse("work_list"),
            reverse("work_list") + "?era=modern&topic=ethics&sort=rating&free=1",
            work.get_absolute_url(),
            reverse("work_reviews", args=[work.slug]),
            reverse("thinker_list"),
            reverse("thinker_list") + "?era=medieval&sort=name",
            reverse("thinker_detail", args=["plato"]),
            reverse("school_list"),
            reverse("school_detail", args=["stoicism"]),
            reverse("topic_list"),
            reverse("topic_detail", args=["ethics"]),
            era.get_absolute_url(),
            reverse("timeline"),
            reverse("quote_list"),
            Quote.objects.first().get_absolute_url(),
        ]
        for url in urls:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)

    def test_work_page_has_structured_data_and_meta(self):
        response = self.client.get(reverse("work_detail", args=["meditations"]))
        self.assertContains(response, '"@type": "Book"')
        self.assertContains(response, "<title>Meditations")
        self.assertContains(response, 'rel="canonical"')
        self.assertContains(response, "Key ideas")

    def test_unknown_filter_is_404(self):
        self.assertEqual(self.client.get(reverse("work_list") + "?era=nope").status_code, 404)
