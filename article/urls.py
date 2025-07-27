# article/urls.py
from django.urls import path
from article.views import home
from article.views import create_article

urlpatterns = [
    path("", home, name="home"),
    path("articles/create/", create_article, name="create_article"),
]
