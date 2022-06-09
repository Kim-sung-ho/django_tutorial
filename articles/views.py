import random
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.


def index(request):
    return render(request, 'index.html')


def dinner(request):
    menus = [{"name": '족발', "price": 30000},
             {"name": '햄버거', "price": 5000},
             {"name": '치킨', "price": 20000},
             {"name": '초밥', "price": 15000},
             ]
    pick = random.choice(menus)
    articles = Article.objects.all()
    # 딕셔너리의 key로 사용할 변수명을 만들고, value로 딕셔너리에 넣어준다.
    context = {
        'pick': pick,
        'menus': menus,
        'articles': articles,
    }
    return render(request, 'dinner.html', context)


def review(request):
    return render(request, 'review.html')

# request 는 요청한 모든데이터들이 들어있다.


def create_review(request):
    content = request.POST.get('content')
    title = request.POST.get('title')
    article = Article(title=title, content=content)
    article.save()
    context = {
        'content': content,
        'article': article,
    }
    return redirect('articles:detail', article.pk)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        article.delete()

    return redirect('articles:dinner')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
