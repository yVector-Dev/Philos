from django.urls import path

from . import views

urlpatterns = [
    path("works/", views.work_list, name="work_list"),
    path("works/<slug:slug>/", views.work_detail, name="work_detail"),
    path("works/<slug:slug>/reviews/", views.work_reviews, name="work_reviews"),
    path("thinkers/", views.thinker_list, name="thinker_list"),
    path("thinkers/<slug:slug>/", views.thinker_detail, name="thinker_detail"),
    path("schools/", views.school_list, name="school_list"),
    path("schools/<slug:slug>/", views.school_detail, name="school_detail"),
    path("topics/", views.topic_list, name="topic_list"),
    path("topics/<slug:slug>/", views.topic_detail, name="topic_detail"),
    path("eras/<slug:slug>/", views.era_detail, name="era_detail"),
    path("timeline/", views.timeline, name="timeline"),
    path("quotes/", views.quote_list, name="quote_list"),
    path("quotes/<int:pk>/", views.quote_detail, name="quote_detail"),
]
