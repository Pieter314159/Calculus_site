from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from .models import Article
from .forms import ArticleForm

# Create your views here.
def post_list(request):
    articles = Article.objects.filter(published_date__lt=timezone.now()).order_by('published_date')
    return render(request, 'articles/post_list.html', {'articles':articles})

def main_articles(request):
    return render(request, 'articles/main_articles.html', {})

def post_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/post_detail.html', {'article':article})

def post_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect('post_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'articles/post_edit.html', {'form':form})

def post_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect('post_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/post_edit.html', {"form":form})
