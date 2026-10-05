from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from accounts import views as account_views
from core import views as core_views
from core.sitemaps import sitemaps

urlpatterns = [
    path("", core_views.home, name="home"),
    path("welcome/", core_views.welcome, name="welcome"),
    path("search/", core_views.search, name="search"),
    path("about/", core_views.about, name="about"),
    path("robots.txt", core_views.robots_txt, name="robots_txt"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("", include("catalog.urls")),
    path("", include("social.urls")),
    # Accounts
    path("accounts/signup/", account_views.signup, name="signup"),
    path("accounts/login/", auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/password/change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("accounts/password/change/done/", auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),
    path("accounts/password/reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("accounts/password/reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("accounts/reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path("accounts/reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("settings/", account_views.settings_view, name="settings"),
    path("admin/", admin.site.urls),
]

handler404 = "core.views.page_not_found"
