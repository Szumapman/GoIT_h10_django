from django.urls import path
from . import views

app_name = "quotes_app"

urlpatterns = [
    path("", views.index, name="index"),
    # path("author/<int:author_id>/", views.author, name="author"),
    # path("tag/<int:tag_id>/", views.tag, name="tag"),
    # path("random/", views.random, name="
]
