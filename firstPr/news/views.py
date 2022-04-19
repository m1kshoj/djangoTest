from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticleFrom


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Wrong form'

    form = ArticleFrom()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
