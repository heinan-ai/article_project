# article/forms.py
from django import forms
from article.models import Article

class CreateArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    status = forms.ChoiceField(
        choices=(
            ("draft", "draft"),
            ("inprogress", "in progress"),
            ("published", "published")
        )
    )
    content = forms.CharField(widget=forms.Textarea)
    word_count = forms.IntegerField()
    twitter_post = forms.CharField(widget=forms.Textarea, required=False)
    
    # class Meta:
    #     model = Article
    #     fields = (
    #         "title",
    #         "status",
    #         "content",
    #         "word_count",
    #         "twitter_post",
    #     )