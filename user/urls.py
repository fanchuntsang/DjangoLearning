from django.conf.urls import url
from django.urls import include

import news
from . import views
urlpatterns = [
    url(r'^login',views.loginView,name='login'),
    url(r'profile',views.profile,name='profile'),
    url(r'deleteComment',views.deleteComment,name='deleteComment'),
    url('register',views.registerView,name='register'),
    url('setpassword',views.setpasswordView,name='setpassword'),
    url('logout',views.logoutView,name='logout'),
    url(r'^$',views.loginView),
    url(r'^news/',include('news.urls',namespace='news')),
    url(r'^novel/',include('novel.urls',namespace='novel')),
    url(r'^comic/',include('comic.urls',namespace='comic')),
]
