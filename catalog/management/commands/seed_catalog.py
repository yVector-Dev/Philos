"""Load (or refresh) the built-in catalogue: eras, schools, topics, thinkers, works, quotes and editorial lists.

Safe to run repeatedly: rows are matched by slug and updated in place, and user data is never touched.
"""

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from catalog.models import Era, Quote, School, Thinker, Topic, Work
from catalog.seed.quotes_lists import EDITORIAL_LISTS, QUOTES
from catalog.seed.taxonomy import ERAS, SCHOOLS, TOPICS
from catalog.seed.thinkers import THINKERS
from catalog.seed.works_classical import WORKS_CLASSICAL
from catalog.seed.works_modern import WORKS_MODERN

EDITOR_USERNAME = "philos"


def era_for_year(eras, year):
    if year is None:
        return None
    for era in eras:
        if era.start_year <= year and (era.end_year is None or year < era.end_year):
            return era
    return eras[0] if year < eras[0].start_year else eras[-1]


class Command(BaseCommand):
    help = "Seed or refresh the built-in catalogue of thinkers, works, quotes and editorial lists."

    def add_arguments(self, parser):
        parser.add_argument("--no-lists", action="store_true", help="Skip the editorial reading lists.")

    @transaction.atomic
    def handle(self, *args, **options):
        eras = {}
        for order, e in enumerate(ERAS):
            eras[e["slug"]], _ = Era.objects.update_or_create(
                slug=e["slug"],
                defaults=dict(
                    name=e["name"], start_year=e["start"], end_year=e["end"], summary=e["summary"],
                    description=e["description"], order=order, color=e["color"],
                ),
            )
        ordered_eras = sorted(eras.values(), key=lambda era: era.start_year)

        schools = {}
        for slug, name, era_slug, summary in SCHOOLS:
            schools[slug], _ = School.objects.update_or_create(
                slug=slug, defaults=dict(name=name, era=eras[era_slug], summary=summary)
            )

        topics = {}
        for slug, name, question, summary in TOPICS:
            topics[slug], _ = Topic.objects.update_or_create(
                slug=slug, defaults=dict(name=name, question=question, summary=summary)
            )

        thinkers = {}
        for t in THINKERS:
            thinker, _ = Thinker.objects.update_or_create(
                slug=t["slug"],
                defaults=dict(
                    name=t["name"], birth_year=t["born"], death_year=t["died"], years_approx=t["approx"],
                    dates_label=t["dates"], birthplace=t["place"], era=eras[t["era"]], tagline=t["tagline"],
                    bio=t["bio"],
                ),
            )
            thinker.schools.set([schools[s] for s in t["schools"]])
            thinker.topics.set([topics[s] for s in t["topics"]])
            thinkers[t["slug"]] = thinker
        for t in THINKERS:
            thinkers[t["slug"]].influences.set([thinkers[s] for s in t["influences"]])

        works = {}
        for w in WORKS_CLASSICAL + WORKS_MODERN:
            author = thinkers[w["author"]]
            work, _ = Work.objects.update_or_create(
                slug=w["slug"],
                defaults=dict(
                    title=w["title"], author=author, year=w["year"], year_approx=w["approx"],
                    era=era_for_year(ordered_eras, w["year"]), kind=w["kind"], original_title=w["original"],
                    original_language=w["lang"], pages=w["pages"], difficulty=w["difficulty"],
                    summary=w["summary"], description=w["description"], key_ideas="\n".join(w["ideas"]),
                    public_domain=w["pd"], featured=w["featured"],
                ),
            )
            work.topics.set([topics[s] for s in w["topics"]])
            work.schools.set(author.schools.all())
            works[w["slug"]] = work

        for thinker_slug, work_slug, source, text in QUOTES:
            Quote.objects.update_or_create(
                thinker=thinkers[thinker_slug],
                text=text,
                defaults=dict(work=works[work_slug] if work_slug else None, source=source),
            )

        lists_count = 0
        if not options["no_lists"]:
            lists_count = self._seed_lists(works)

        self.stdout.write(self.style.SUCCESS(
            f"Catalogue ready: {len(eras)} eras, {len(schools)} schools, {len(topics)} topics, "
            f"{len(thinkers)} thinkers, {len(works)} works, {len(QUOTES)} quotes, {lists_count} editorial lists."
        ))

    def _seed_lists(self, works):
        from social.models import ListItem, ReadingList

        User = get_user_model()
        editor, created = User.objects.get_or_create(
            username=EDITOR_USERNAME,
            defaults=dict(
                display_name="Philos Editors",
                bio="Curated reading paths through the great books of philosophy and history.",
            ),
        )
        if created:
            editor.set_unusable_password()
            editor.save()

        for title, ranked, description, slugs in EDITORIAL_LISTS:
            reading_list = ReadingList.objects.filter(user=editor, title=title).first()
            if reading_list is None:
                reading_list = ReadingList(user=editor, title=title)
            reading_list.description = description
            reading_list.is_ranked = ranked
            reading_list.is_editorial = True
            reading_list.save()
            reading_list.items.all().delete()
            ListItem.objects.bulk_create(
                ListItem(reading_list=reading_list, work=works[slug], position=i) for i, slug in enumerate(slugs)
            )
        return len(EDITORIAL_LISTS)
