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
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpRequest, HttpResponse




class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "article/home.html"
    model = Article
    context_object_name = "articles"
    
    def get_queryset(self):
        return Article.objects.filter(creator=self.request.user).order_by("-created_at")
    

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article/create_article.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")
    
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "article/update_article.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name = "article"
    
    def test_func(self):
        return self.request.user == self.get_object().creator

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    template_name = "article/delete_article.html"
    model = Article
    success_url = reverse_lazy("home")
    # success_message = "Article deleted successfully."
    context_object_name = "article"
    
    def test_func(self):
        return self.request.user == self.get_object().creator
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        messages.success(request, "Article deleted successfully.", extra_tags="destructive")
        return super().post(request, *args, **kwargs) 