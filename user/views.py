from itertools import chain

from django.contrib.auth.decorators import login_required
import json
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from comment.models import Comment
from collect.models import Collect

# Create your views here.
NEWSTYPE = 1
NOVELTYPE = 2
COMICTYPE = 3
def loginView(request):
    # 设置标题和另外两个URL链接
    title = '登录'
    unit_2 = '/user/register.html'
    unit_2_name = '立即注册'
    unit_1 = '/user/setpassword.html'
    unit_1_name = '修改密码'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                return redirect('/')
            else:
                tips = '账号密码错误，请重新输入'
        else:
            tips = '用户不存在，请注册'
    return render(request, 'user2.html', locals())

# 用户注册
def registerView(request):
    # 设置标题和另外两个URL链接
    title = '注册'
    unit_2 = '/user/login.html'
    unit_2_name = '立即登录'
    unit_1 = '/user/setpassword.html'
    unit_1_name = '修改密码'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            tips = '用户已存在'
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            tips = '注册成功，请登录'
    return render(request, 'user2.html', locals())

# 修改密码
def setpasswordView(request):
    # 设置标题和另外两个URL链接
    title = '修改密码'
    unit_2 = '/user/login.html'
    unit_2_name = '立即登录'
    unit_1 = '/user/register.html'
    unit_1_name = '立即注册'
    new_password = True
    if request.method == 'POST':
        username = request.POST.get('username', '')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username,password=old_password)
            # 判断用户的账号密码是否正确
            if user:
                user.set_password(new_password)
                user.save()
                tips = '密码修改成功'
            else:
                tips = '原始密码不正确'
        else:
            tips = '用户不存在'
    return render(request, 'user2.html', locals())

# 使用make_password实现密码修改
from django.contrib.auth.hashers import make_password
def setpasswordView_1(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        # 判断用户是否存在
        user = User.objects.filter(username=username)
        if User.objects.filter(username=username):
            user = authenticate(username=username,password=old_password)
            # 判断用户的账号密码是否正确
            if user:
                # 密码加密处理并保存到数据库
                dj_ps = make_password(new_password, None, 'pbkdf2_sha256')
                user.password = dj_ps
                user.save()
            else:
                print('原始密码不正确')
    return render(request, 'user2.html', locals())

# 用户注销，退出登录
def logoutView(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    userid = request.session.get('_auth_user_id')
    username = User.objects.get(id=userid)
    comment = Comment.objects.filter(user=userid)
    news_collect = Collect.objects.filter(Q(user=userid)&Q(collect_type=NEWSTYPE))
    novel_collect = Collect.objects.filter(Q(user=userid)&Q(collect_type=NOVELTYPE))
    comic_collect = Collect.objects.filter(Q(user=userid)&Q(collect_type=COMICTYPE))
    context_json = chain(comment,news_collect,novel_collect,comic_collect)
    context = {"username":username,"userid":userid,"comment":comment,"news_collect":news_collect,"novel_collect":novel_collect,"comic_collect":comic_collect}

    # return HttpResponse("开发中")
    return render(request,"profile.html",context)

@login_required
def deleteComment(request):
    commentId = request.GET['commentId']
    comment = Comment.objects.filter(comment_id=commentId).delete()
    return HttpResponse("删除成功")


