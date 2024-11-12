from django.urls import path
from . import views

urlpatterns = [
    path("", views.article_home, name="article_home"),
    path("<article_id>", views.view_article, name="view_article"),
]