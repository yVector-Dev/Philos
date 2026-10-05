from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from catalog.models import Work


class AccountTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_catalog", verbosity=0)

    def test_signup_logs_in_and_goes_to_welcome(self):
        response = self.client.post(reverse("signup"), {
            "username": "new_reader", "email": "New@Example.com",
            "password1": "a-long-pass-phrase-1", "password2": "a-long-pass-phrase-1",
        })
        self.assertRedirects(response, reverse("welcome"))
        user = User.objects.get(username="new_reader")
        self.assertEqual(user.email, "new@example.com")
        self.assertEqual(self.client.get(reverse("welcome")).status_code, 200)

    def test_signup_rejects_bad_or_duplicate_usernames(self):
        User.objects.create_user("taken", "t@example.com", "pw-123-abc!")
        for username in ("Taken", "a b", "x", "bad/name"):
            response = self.client.post(reverse("signup"), {
                "username": username, "email": f"{len(username)}@example.com",
                "password1": "a-long-pass-phrase-1", "password2": "a-long-pass-phrase-1",
            })
            self.assertEqual(response.status_code, 200, username)
        self.assertEqual(User.objects.count(), 2)  # 'taken' + the editorial account

    def test_settings_saves_profile_and_favourites(self):
        user = User.objects.create_user("reader", "r@example.com", "pw-123-abc!")
        self.client.force_login(user)
        works = list(Work.objects.order_by("id")[:2])
        response = self.client.post(reverse("settings"), {
            "display_name": "Reader", "bio": "Hi", "location": "Lisbon", "website": "https://example.com",
            "slot_0": works[0].pk, "slot_1": works[1].pk, "slot_2": works[0].pk, "slot_3": "",
        })
        self.assertRedirects(response, reverse("profile", args=["reader"]))
        user.refresh_from_db()
        self.assertEqual(user.display_name, "Reader")
        self.assertEqual([f.work_id for f in user.favorite_links.all()], [works[0].pk, works[1].pk])

    def test_settings_rejects_javascript_urls(self):
        user = User.objects.create_user("reader2", "r2@example.com", "pw-123-abc!")
        self.client.force_login(user)
        response = self.client.post(reverse("settings"), {"website": "javascript:alert(1)"})
        self.assertEqual(response.status_code, 200)
        user.refresh_from_db()
        self.assertEqual(user.website, "")

    def test_auth_pages_render(self):
        for name in ("login", "signup", "password_reset"):
            self.assertEqual(self.client.get(reverse(name)).status_code, 200)
