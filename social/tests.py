from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from catalog.models import Work
from social.models import Comment, Entry, Follow, ListItem, ReadingList, UserWork

XHR = {"HTTP_X_REQUESTED_WITH": "XMLHttpRequest"}


class SocialTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_catalog", verbosity=0)
        cls.alice = User.objects.create_user("alice", "alice@example.com", "pw-alice-123!")
        cls.bob = User.objects.create_user("bob", "bob@example.com", "pw-bob-123!")
        cls.work = Work.objects.get(slug="republic")

    def setUp(self):
        self.client.force_login(self.alice)

    def status(self, action, **extra):
        return self.client.post(reverse("work_status", args=[self.work.slug]), {"action": action, **extra}, **XHR)

    def test_read_like_want_and_rate_update_stats(self):
        data = self.status("read").json()
        self.assertTrue(data["is_read"])
        self.assertEqual(data["stats"]["read_count"], 1)

        data = self.status("rate", rating=7).json()
        self.assertEqual(data["rating"], 7)
        self.assertEqual(data["stats"]["rating_avg_5"], 3.5)

        data = self.status("like").json()
        self.assertTrue(data["is_liked"])

        data = self.status("read").json()  # un-reading clears rating and like
        self.assertFalse(data["is_read"])
        self.assertIsNone(data["rating"])
        self.assertEqual(data["stats"]["read_count"], 0)
        self.assertFalse(UserWork.objects.filter(user=self.alice, work=self.work).exists())

    def test_want_to_read_then_read_moves_off_list(self):
        self.status("want")
        self.assertTrue(UserWork.objects.get(user=self.alice, work=self.work).want_to_read)
        self.status("rate", rating=10)
        state = UserWork.objects.get(user=self.alice, work=self.work)
        self.assertTrue(state.is_read)
        self.assertFalse(state.want_to_read)

    def test_status_requires_login_and_post(self):
        self.client.logout()
        response = self.client.post(reverse("work_status", args=[self.work.slug]), {"action": "read"})
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.alice)
        self.assertEqual(self.client.get(reverse("work_status", args=[self.work.slug])).status_code, 405)
        self.assertEqual(self.status("explode").status_code, 400)

    def test_non_ajax_status_redirects_safely(self):
        response = self.client.post(
            reverse("work_status", args=[self.work.slug]), {"action": "read", "next": "https://evil.example/"}
        )
        self.assertRedirects(response, self.work.get_absolute_url(), fetch_redirect_response=False)

    def test_log_with_review_creates_entry_and_review_page(self):
        response = self.client.post(
            reverse("log_work", args=[self.work.slug]),
            {"rating": 9, "review": "The cave <script>alert(1)</script> still works.", "read_on": "2026-01-02",
             "liked": "on"},
        )
        entry = Entry.objects.get(user=self.alice, work=self.work)
        self.assertRedirects(response, entry.get_absolute_url())
        self.work.refresh_from_db()
        self.assertEqual((self.work.review_count, self.work.read_count, self.work.like_count), (1, 1, 1))

        page = self.client.get(entry.get_absolute_url())
        self.assertContains(page, "&lt;script&gt;")
        self.assertNotContains(page, "<script>alert(1)</script>")
        self.assertContains(page, '"@type": "Review"')
        self.assertContains(self.client.get(self.work.get_absolute_url()), "Review by")

    def test_log_page_renders(self):
        self.assertEqual(self.client.get(reverse("log_work", args=[self.work.slug])).status_code, 200)

    def test_only_owner_can_edit_or_delete_review(self):
        entry = Entry.objects.create(user=self.bob, work=self.work, review="Mine")
        edit = reverse("review_edit", args=["bob", entry.pk])
        delete = reverse("review_delete", args=["bob", entry.pk])
        self.assertEqual(self.client.get(edit).status_code, 403)
        self.assertEqual(self.client.post(delete).status_code, 403)
        self.assertTrue(Entry.objects.filter(pk=entry.pk).exists())
        # wrong username in URL is a 404
        self.assertEqual(self.client.get(reverse("review_detail", args=["alice", entry.pk])).status_code, 404)

    def test_like_and_comment_review(self):
        entry = Entry.objects.create(user=self.bob, work=self.work, review="Thoughts")
        like_url = reverse("review_like", args=["bob", entry.pk])
        self.assertEqual(self.client.post(like_url, **XHR).json(), {"liked": True, "count": 1})
        self.assertEqual(self.client.post(like_url, **XHR).json(), {"liked": False, "count": 0})

        self.client.post(reverse("comment_create", args=["bob", entry.pk]), {"body": "Agreed!"})
        entry.refresh_from_db()
        self.assertEqual(entry.comment_count, 1)
        comment = Comment.objects.get()
        # bob (review owner) may delete alice's comment; a third party may not
        carol = User.objects.create_user("carol", "c@example.com", "pw-carol-123!")
        self.client.force_login(carol)
        self.assertEqual(self.client.post(reverse("comment_delete", args=[comment.pk])).status_code, 403)
        self.client.force_login(self.bob)
        self.client.post(reverse("comment_delete", args=[comment.pk]))
        self.assertFalse(Comment.objects.exists())

    def test_follow_toggle_and_feed(self):
        url = reverse("follow_toggle", args=["bob"])
        self.assertTrue(self.client.post(url, **XHR).json()["following"])
        Entry.objects.create(user=self.bob, work=self.work, rating=8)
        feed = self.client.get(reverse("activity"))
        self.assertContains(feed, "The Republic")
        self.assertFalse(self.client.post(url, **XHR).json()["following"])
        self.client.post(reverse("follow_toggle", args=["alice"]))
        self.assertFalse(Follow.objects.filter(follower=self.alice, followed=self.alice).exists())

    def test_lists_create_add_move_remove(self):
        response = self.client.post(reverse("list_create") + "?add=republic", {"title": "My Shelf", "add": "republic"})
        rl = ReadingList.objects.get(user=self.alice)
        self.assertRedirects(response, rl.get_absolute_url())
        self.assertEqual(rl.slug, "my-shelf")
        other = Work.objects.get(slug="meditations")
        self.assertTrue(self.client.post(reverse("list_toggle_item"), {"list": rl.pk, "work": other.pk}, **XHR)
                        .json()["added"])
        first, second = rl.items.all()
        self.client.post(reverse("list_move_item", args=[second.pk]), {"direction": "up"})
        self.assertEqual([i.work.slug for i in rl.items.all()], ["meditations", "republic"])
        self.assertFalse(self.client.post(reverse("list_toggle_item"), {"list": rl.pk, "work": other.pk}, **XHR)
                         .json()["added"])
        self.assertEqual(rl.items.count(), 1)
        self.assertEqual(self.client.get(rl.get_absolute_url()).status_code, 200)

    def test_cannot_modify_someone_elses_list(self):
        rl = ReadingList.objects.create(user=self.bob, title="Bob's")
        item = ListItem.objects.create(reading_list=rl, work=self.work)
        self.assertEqual(self.client.post(reverse("list_toggle_item"), {"list": rl.pk, "work": self.work.pk}).status_code, 404)
        self.assertEqual(self.client.post(reverse("list_move_item", args=[item.pk]), {"direction": "up"}).status_code, 404)
        self.assertEqual(self.client.get(reverse("list_edit", args=["bob", rl.slug])).status_code, 403)
        self.assertEqual(self.client.post(reverse("list_delete", args=["bob", rl.slug])).status_code, 403)

    def test_duplicate_list_titles_get_unique_slugs(self):
        a = ReadingList.objects.create(user=self.alice, title="Stoics")
        b = ReadingList.objects.create(user=self.alice, title="Stoics")
        self.assertEqual((a.slug, b.slug), ("stoics", "stoics-2"))

    def test_profile_pages(self):
        Entry.objects.create(user=self.alice, work=self.work, rating=8, review="Great")
        UserWork.objects.create(user=self.alice, work=self.work, is_read=True, rating=8)
        for name in ("profile", "profile_diary", "profile_reviews", "profile_works", "profile_to_read",
                     "profile_likes", "profile_lists", "profile_following", "profile_followers"):
            with self.subTest(name=name):
                self.assertEqual(self.client.get(reverse(name, args=["alice"])).status_code, 200)
        self.assertEqual(self.client.get(reverse("profile", args=["nobody"])).status_code, 404)
