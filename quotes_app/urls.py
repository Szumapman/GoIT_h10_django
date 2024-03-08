"""Urls patterns for quotes_app."""

from django.urls import path
from . import views

app_name = "quotes_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("author/<int:author_id>/", views.author, name="author"),
    path("new_author/", views.new_author, name="new_author"),
    path("new_tag/", views.new_tag, name="new_tag"),
    path("new_quote/", views.new_quote, name="new_quote"),
    path("scrape_data/", views.scrape_data, name="scrape_data"),
    # path("tag/<int:tag_id>/", views.tag, name="tag"),
    # path("random/", views.random, name="
]
