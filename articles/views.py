from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def article_home(request):
    all_articles = Article.objects.all()

    context = {
        'articles': all_articles,
    }

    return render(request, 'articles/index.html', context)

def view_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    context = { 'article': article, }

    return render(request, 'articles/article.html', context)