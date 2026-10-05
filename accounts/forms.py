import re

from django import forms
from django.contrib.auth.forms import UserCreationForm

from catalog.models import Work

from .models import User

USERNAME_RE = re.compile(r"^[A-Za-z0-9_]{3,30}$")


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Used only for password resets. Never shown publicly.")

    class Meta:
        model = User
        fields = ("username", "email")
        help_texts = {"username": "3–30 letters, numbers or underscores. This is your public URL."}

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not USERNAME_RE.match(username):
            raise forms.ValidationError("Use 3–30 letters, numbers or underscores.")
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("That username is taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("display_name", "bio", "location", "website")
        widgets = {"bio": forms.Textarea(attrs={"rows": 4})}
        labels = {"display_name": "Display name"}


class FavoritesForm(forms.Form):
    """Four optional slots for a user's favourite works."""

    SLOTS = 4

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        works = Work.objects.select_related("author").order_by("title")
        current = list(user.favorite_links.select_related("work")) if user else []
        for i in range(self.SLOTS):
            self.fields[f"slot_{i}"] = forms.ModelChoiceField(
                queryset=works, required=False, label=f"Favourite #{i + 1}", empty_label="—"
            )
            if i < len(current):
                self.initial[f"slot_{i}"] = current[i].work_id

    def chosen_works(self):
        seen, works = set(), []
        for i in range(self.SLOTS):
            work = self.cleaned_data.get(f"slot_{i}")
            if work and work.pk not in seen:
                seen.add(work.pk)
                works.append(work)
        return works
