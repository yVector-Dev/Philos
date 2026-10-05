from django.contrib import admin

from .models import Era, Quote, School, Thinker, Topic, Work


@admin.register(Era)
class EraAdmin(admin.ModelAdmin):
    list_display = ("name", "start_year", "end_year", "order")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name", "era")
    list_filter = ("era",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name", "question")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Thinker)
class ThinkerAdmin(admin.ModelAdmin):
    list_display = ("name", "lifespan", "era")
    list_filter = ("era", "schools")
    search_fields = ("name", "tagline")
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ("schools", "topics", "influences")


class QuoteInline(admin.TabularInline):
    model = Quote
    extra = 0
    fields = ("text", "thinker", "source")


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "year", "era", "read_count", "rating_avg", "featured")
    list_filter = ("era", "kind", "featured", "public_domain", "topics")
    search_fields = ("title", "original_title", "author__name")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("author",)
    filter_horizontal = ("topics", "schools")
    readonly_fields = ("rating_avg", "rating_count", "read_count", "like_count", "want_count", "review_count")
    inlines = [QuoteInline]


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("__str__", "thinker", "work")
    search_fields = ("text", "thinker__name")
    autocomplete_fields = ("thinker", "work")
