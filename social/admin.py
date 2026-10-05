from django.contrib import admin

from .models import Comment, Entry, Follow, ListItem, ReadingList, UserWork


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("user", "work", "rating", "has_review", "like_count", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "work__title", "review")
    raw_id_fields = ("user", "work")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "entry", "created_at")
    search_fields = ("body", "user__username")
    raw_id_fields = ("user", "entry")


class ListItemInline(admin.TabularInline):
    model = ListItem
    extra = 0
    raw_id_fields = ("work",)


@admin.register(ReadingList)
class ReadingListAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "is_editorial", "like_count", "updated_at")
    list_filter = ("is_editorial",)
    search_fields = ("title", "user__username")
    raw_id_fields = ("user",)
    inlines = [ListItemInline]


@admin.register(UserWork)
class UserWorkAdmin(admin.ModelAdmin):
    list_display = ("user", "work", "is_read", "is_liked", "want_to_read", "rating")
    raw_id_fields = ("user", "work")


admin.site.register(Follow)
