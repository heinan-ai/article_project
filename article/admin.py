# article/admin.py

from django.contrib import admin
from article.models import Article, UserProfile

admin.site.register(Article)
admin.site.register(UserProfile)
