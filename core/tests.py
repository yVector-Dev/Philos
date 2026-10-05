from django.core.management import call_command
from django.test import TestCase, override_settings
from django.urls import reverse

from accounts.models import User
from catalog.models import Work
from social.models import Entry


@override_settings(SITE_URL="https://philos.example")
class CoreTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_catalog", verbosity=0)

    def test_home_logged_out_and_in(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Read the books that shaped civilization.")
        self.assertContains(response, "Thought for today")
        user = User.objects.create_user("reader", "r@example.com", "pw-123-abc!")
        self.client.force_login(user)
        self.assertContains(self.client.get(reverse("home")), "Welcome back")

    def test_search(self):
        response = self.client.get(reverse("search"), {"q": "stoic"})
        self.assertContains(response, "Stoicism")
        self.assertContains(self.client.get(reverse("search"), {"q": "plato"}), "The Republic")
        self.assertEqual(self.client.get(reverse("search")).status_code, 200)

    def test_robots_and_sitemap(self):
        robots = self.client.get("/robots.txt")
        self.assertContains(robots, "Sitemap: https://philos.example/sitemap.xml")
        user = User.objects.create_user("reader", "r@example.com", "pw-123-abc!")
        entry = Entry.objects.create(user=user, work=Work.objects.get(slug="republic"), review="Yes.")
        sitemap = self.client.get("/sitemap.xml")
        self.assertEqual(sitemap.status_code, 200)
        self.assertContains(sitemap, "https://philos.example/works/republic/")
        self.assertContains(sitemap, "https://philos.example/thinkers/plato/")
        self.assertContains(sitemap, "https://philos.example" + entry.get_absolute_url())

    def test_canonical_uses_site_url(self):
        self.assertContains(self.client.get("/works/"), '<link rel="canonical" href="https://philos.example/works/">')

    def test_404_page(self):
        response = self.client.get("/does-not-exist/")
        self.assertEqual(response.status_code, 404)

    def test_about(self):
        self.assertContains(self.client.get(reverse("about")), "Philosophy is for everyone.")
