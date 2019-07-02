from django.http import HttpResponse
from django.shortcuts import render

from news.models import News
from novel.models import Novel
from comic.models import Comic


def hello(request):
    news = News.objects.filter().order_by('-news_id')[0:5]
    novel = Novel.objects.filter().order_by('-novel_grade')[0:5]
    comic = Comic.objects.filter().order_by('-comic_grade')[0:15]
    context = {'news':news,'novel':novel,'comic':comic}
    username = request.user.username
    return render(request, 'index.html', context)

def hello2(request):
    return render(request, 'hello.html')

def search(request):
    return HttpResponse(request.POST['search'])
