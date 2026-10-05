from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import FavoriteWork, User


class FavoriteInline(admin.TabularInline):
    model = FavoriteWork
    extra = 0
    raw_id_fields = ("work",)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (("Profile", {"fields": ("display_name", "bio", "location", "website")}),)
    list_display = ("username", "display_name", "email", "date_joined", "is_staff")
    inlines = [FavoriteInline]
