from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['headline', 'image', 'author', 'copy']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'article', 'text']