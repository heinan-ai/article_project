# article/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from article.models import Article
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)



class ArticleListView(ListView):
    template_name = "article/home.html"
    model = Article
    context_object_name = "articles"
    

class ArticleCreateView(CreateView):
    template_name = "article/create_article.html"
    model = Article
    fields = ["title", "status", "content", "word_count", "twitter_post"]
    success_url = reverse_lazy("home")
    

class ArticleUpdateView(UpdateView):
    template_name = "article/update_article.html"
    model = Article
    fields = ["title", "status", "content", "word_count", "twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name = "article"

class ArticleDeleteView(DeleteView):
    template_name = "article/delete_article.html"
    model = Article
    success_url = reverse_lazy("home")
    context_object_name = "article"