"""Keep denormalised counters in sync with the rows they summarise."""

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from catalog.models import Work

from .models import Comment, Entry, EntryLike, ListLike, ReadingList, UserWork


def _refresh_work(work_id):
    work = Work.objects.filter(pk=work_id).first()
    if work:
        work.refresh_stats()


@receiver([post_save, post_delete], sender=UserWork)
@receiver([post_save, post_delete], sender=Entry)
def update_work_stats(sender, instance, **kwargs):
    _refresh_work(instance.work_id)


@receiver([post_save, post_delete], sender=EntryLike)
@receiver([post_save, post_delete], sender=Comment)
def update_entry_counts(sender, instance, **kwargs):
    entry = Entry.objects.filter(pk=instance.entry_id).first()
    if entry:
        entry.refresh_counts()


@receiver([post_save, post_delete], sender=ListLike)
def update_list_counts(sender, instance, **kwargs):
    reading_list = ReadingList.objects.filter(pk=instance.reading_list_id).first()
    if reading_list:
        reading_list.refresh_counts()
