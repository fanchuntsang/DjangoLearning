from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from collect.models import Collect
from . import models
from comic.models import Comic
from comic.models import ComicType
from django.contrib.auth.models import User
from comment.models import Comment
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
COMICTYPE = 3

def ComicIndex(request):
    comic = models.Comic.objects.filter()
    comicType = ComicType.objects.filter()
    paginator = Paginator(comic, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page) # contacts为Page对象！
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    context = {'comic': comic,'type':comicType,'contacts': contacts}
    return render(request, 'ComiclList.html', context)

def ComicDetail(request,comic_id):#无指定章节就进入漫画详情，有指定就进入章节内
    userid = request.session.get('_auth_user_id')
    flag=""
    state=""
    if Collect.objects.filter(Q(user_id=userid)&Q(collect_type=COMICTYPE)&Q(collect_in_id=comic_id)).count()==0 :
        flag = "未收藏"
    else:
        flag = "已收藏"
    if(request.GET.get('chapter')== None or request.GET.get('chapter')==''):
        comic = models.Comic.objects.get(comic_id=comic_id)
        comic.comic_grade+=1;
        comic.save();
        if(comic.comic_state==True):
            state="已完结"
        else:
            state="连载中"
        chapter = models.ComicChapter.objects.filter(comic=comic_id)
        comment = Comment.objects.filter(Q(comment_in_id=comic_id)&Q(comment_type=3)).order_by('-comment_id')[0:5]
        context={'comic':comic,'chapter':chapter,'comment':comment,'flag':flag,'state':state}
        return  render(request,"comic_details.html",context)
    chapter=request.GET.get('chapter')
    comic = models.ComicChapter.objects.get(Q(comic_id=comic_id)&Q(cchapter_id=chapter))
    context = {'comic':comic,'flag':flag}
    return render(request,"comic_chapter_details.html",context)

def ComicTypeList(request,comictype_id):
    comic = models.Comic.objects.filter(comic_type=comictype_id)
    comics= models.Comic.objects.filter(comic_type=comictype_id)
    comicType = ComicType.objects.filter()
    paginator = Paginator(comic, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page) # contacts为Page对象！
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    context={'comic': comic,'comics':comics,'type':comicType,'contacts': contacts}
    return render(request,"comic_type.html",context)

@login_required
def ComicComment(request):
    if request.method == 'POST':
        userid = request.session.get('_auth_user_id')
        comicid = int(request.POST['comicid'])
        comment = request.POST['comment']
        ctype = int(request.POST['ctype'])
        print(comment)
        print(comicid)
        print(ctype)
        user = User.objects.get(id=userid)
        Comment.objects.create(user_id=userid,comment_type=ctype,comment_in_id=comicid,comment_content=comment)
        return HttpResponse("评论成功")


@login_required
def comicCollect(request):
    userid = request.session.get('_auth_user_id')
    comic_id = int(request.GET['comic_id'])
    comic = Comic.objects.get(comic_id=comic_id)
    if Collect.objects.filter(Q(user_id=userid)&Q(collect_type=COMICTYPE)&Q(collect_in_id=comic_id)).count()==0 :
        Collect.objects.create(user_id=userid,collect_type=COMICTYPE,collect_in_id=comic_id,collect_name=comic.comic_name)
        comic.comic_collectnum+=1
        comic.save()
        return HttpResponse("收藏成功")
    else:
        Collect.objects.filter(Q(user_id=userid)&Q(collect_type=COMICTYPE)&Q(collect_in_id=comic_id)).delete()
        comic.comic_collectnum-=1
        comic.save()
        return HttpResponse("取消收藏成功")
