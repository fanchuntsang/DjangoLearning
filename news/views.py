from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from comment.models import Comment
from news.models import News
from collect.models import Collect
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

NEWSTYPE = 1

def NewsIndex(request):
    news = News.objects.filter().order_by('-news_uploaddate')
    paginator = Paginator(news, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page) # contacts为Page对象！
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    context = {'news':news,'contacts': contacts}
    return render(request,'NewsList.html',context)

def NewsDetail(request,news_id):
    flag=""
    news = News.objects.get(news_id=news_id)
    news.news_clickNum+=1
    news.save()
    userid = request.session.get('_auth_user_id')
    comment = Comment.objects.filter(Q(comment_in_id=news_id)&Q(comment_type=1)).order_by('-comment_id')[0:5]
    if Collect.objects.filter(Q(user_id=userid)&Q(collect_type=NEWSTYPE)&Q(collect_in_id=news_id)).count()==0 :
        flag = "未收藏"
    else:
        flag = "已收藏"
    context = {'news':news,'comment':comment,'flag':flag}
    return render(request,"news_details.html",context)

@login_required
def NewsComment(request):
    if request.method == 'POST':
        userid = request.session.get('_auth_user_id')
        newsid = int(request.POST['newsid'])
        comment = request.POST['comment']
        ctype = int(request.POST['ctype'])
        print(comment)
        print(newsid)
        print(ctype)
        user = User.objects.get(id=userid)
        Comment.objects.create(user_id=userid,comment_type=ctype,comment_in_id=newsid,comment_content=comment)
        messages.add_message(request,messages.SUCCESS,'评论成功！')
        return HttpResponse("评论成功")

@login_required
def newsCollect(request):
    userid = request.session.get('_auth_user_id')
    getUser = User.objects.get(id=userid)
    news_id = int(request.GET['news_id'])
    news = News.objects.get(news_id=news_id)
    if Collect.objects.filter(Q(user_id=userid)&Q(collect_type=NEWSTYPE)&Q(collect_in_id=news_id)).count()==0 :
        Collect.objects.create(user_id=userid,collect_type=NEWSTYPE,collect_in_id=news_id,collect_name=news.news_title)
        return HttpResponse("收藏成功")
    else:
        Collect.objects.filter(Q(user_id=userid)&Q(collect_type=NEWSTYPE)&Q(collect_in_id=news_id)).delete()
        return HttpResponse("取消收藏成功")
