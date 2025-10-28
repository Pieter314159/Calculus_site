from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'articles/post_list.html', {})

def main_articles(request):
    return render(request, 'articles/main_articles.html', {})