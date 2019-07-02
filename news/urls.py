from django.conf.urls import url
from . import views
app_name = 'news'
urlpatterns = [
    url(r'^index/$',views.NewsIndex,name='NewsIndex'),
    url(r'^$',views.NewsIndex,name='NewsIndex'),
    url(r'^detail/(?P<news_id>[0-9]{1,2})+$',views.NewsDetail,name='NewsDetail'),
    url(r'^NewsComment/$',views.NewsComment,name='NewsComment'),
    url(r'^collect/$',views.newsCollect,name='newsCollect'),
]
