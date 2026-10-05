from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render

from .forms import FavoritesForm, ProfileForm, SignUpForm
from .models import FavoriteWork


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            messages.success(request, "Welcome to Philos! Start by marking a few works you've read.")
            return redirect("welcome")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def settings_view(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=request.user)
        favorites_form = FavoritesForm(request.POST, user=request.user)
        if profile_form.is_valid() and favorites_form.is_valid():
            with transaction.atomic():
                profile_form.save()
                request.user.favorite_links.all().delete()
                FavoriteWork.objects.bulk_create(
                    FavoriteWork(user=request.user, work=work, position=i)
                    for i, work in enumerate(favorites_form.chosen_works())
                )
            messages.success(request, "Profile saved.")
            return redirect("profile", username=request.user.username)
    else:
        profile_form = ProfileForm(instance=request.user)
        favorites_form = FavoritesForm(user=request.user)
    return render(request, "accounts/settings.html", {"profile_form": profile_form, "favorites_form": favorites_form})
