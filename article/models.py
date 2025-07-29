# article/models.py

import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy


class UserProfile(AbstractUser):
    pass


class Article(models.Model):
    
    class Meta:
        verbose_name = gettext_lazy("Article")
        verbose_name_plural = gettext_lazy("Articles")
        
    
    title = models.CharField(gettext_lazy("title"), max_length=100)
    content = models.TextField(gettext_lazy("content"), blank=True, default="")
    word_count = models.IntegerField(gettext_lazy("word count"), blank=True, default="")
    twitter_post = models.TextField(gettext_lazy("twitter post"), blank=True, default="")
    status = models.CharField(
        gettext_lazy("status"),
        max_length=20,
        choices=(
            ("draft", "draft"),
            ("inprogress", "in progress"),
            ("published", "published"),
            ),
        default="draft"
    )
    created_at = models.DateTimeField(gettext_lazy("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(gettext_lazy("updated at"), auto_now=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=gettext_lazy("writer"), on_delete=models.CASCADE, related_name="artiles")
    
    
    def save(self, *args, **kwargs):
        text = re.sub(r"<[^>]*", "", self.content).replace("&nbsp", " ")
        self.word_count = len(re.findall(r"\b\w+\b", text))
        super().save(*args, **kwargs)
    
    