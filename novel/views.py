from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from collect.models import Collect
from novel.models import Novel
from novel.models import NovelType
from comment.models import Comment
from django.contrib.auth.models import User
from . import models
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F


# Create your views here.
NOVELTYPE = 2

def NovelIndex(request):
    novel = Novel.objects.filter()
    novelType = NovelType.objects.filter()
    context = {'novel': novel,'type':novelType}
    return render(request, 'NovelList.html', context)

def NovelDetail(request,novel_id):
    userid = request.session.get('_auth_user_id')
    flag=""
    state=""
    #收藏状态
    if Collect.objects.filter(Q(user_id=userid)&Q(collect_type=NOVELTYPE)&Q(collect_in_id=novel_id)).count()==0 :
        flag = "未收藏"
    else:
        flag = "已收藏"
    if(request.GET.get('chapter')== None or request.GET.get('chapter')==''):#chapter参数为空
        novel = models.Novel.objects.get(novel_id=novel_id) #获取小说
        novel.novel_grade+=1
        novel.save()
        if(novel.novel_state==True):
            state="已完结"
        else:
            state="连载中"
        chapter = models.NovelChapter.objects.filter(novel=novel_id) #获取所有章节
        comment = Comment.objects.filter(Q(comment_in_id=novel_id)&Q(comment_type=2)).order_by('-comment_id')[0:5]
        context={'novel':novel,'chapter':chapter,'comment':comment,'flag':flag,'state':state}
        return  render(request,"novel_details.html",context)
    chapter=request.GET.get('chapter')
    print(novel_id,chapter)
    novel=models.NovelChapter.objects.get(Q(novel=novel_id)&Q(nchapter_id=chapter));
    context ={'novel':novel,'flag':flag}
    return render(request,"novel_chapter_details.html",context)


def NovelTypeList(request,noveltype_id):
    novel = models.Novel.objects.filter(novel_type=noveltype_id)
    novelType = NovelType.objects.filter()
    context={'novel':novel,'type':novelType}
    return render(request,"novel_type.html",context)

@login_required
def NovelComment(request):
    if request.method == 'POST':
        userid = request.session.get('_auth_user_id')
        novelid = int(request.POST['novelid'])
        comment = request.POST['comment']
        ctype = int(request.POST['ctype'])
        print(comment)
        print(novelid)
        print(ctype)
        user = User.objects.get(id=userid)
        Comment.objects.create(user_id=userid,comment_type=ctype,comment_in_id=novelid,comment_content=comment)
        return HttpResponse("评论成功")

# def NovelChapterDetail(request):
#     novelid = request.GET.get('novel')
#     chapter = request.GET.get('chapter')
#     print(novelid,chapter)
#     novel=models.NovelChapter.objects.get(Q(novel=novelid)&Q(nchapter_id=chapter));
#     context ={'novel':novel}
#     return render(request,"novel_chapter_details",context)

@login_required
def novelCollect(request):
    userid = request.session.get('_auth_user_id')
    novel_id = int(request.GET['novel_id'])
    novel = Novel.objects.get(novel_id=novel_id)
    if Collect.objects.filter(Q(user_id=userid)&Q(collect_type=NOVELTYPE)&Q(collect_in_id=novel_id)).count()==0 :
        Collect.objects.create(user_id=userid,collect_type=NOVELTYPE,collect_in_id=novel_id,collect_name=novel.novel_name)
        novel.novel_collectnum+=1;
        novel.save()
        return HttpResponse("收藏成功")
    else:
        Collect.objects.filter(Q(user_id=userid)&Q(collect_type=NOVELTYPE)&Q(collect_in_id=novel_id)).delete()
        novel.novel_collectnum-=1;
        novel.save()
        return HttpResponse("取消收藏成功")
