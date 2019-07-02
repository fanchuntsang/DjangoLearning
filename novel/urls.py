from django.conf.urls import url
from . import views
app_name = 'novel'
urlpatterns = [
    url(r'^index/$',views.NovelIndex,name='NovelIndex'),
    url(r'^$',views.NovelIndex,name='NovelIndex'),
    url(r'^detail/(?P<novel_id>[0-9]{1,2})+$',views.NovelDetail,name='NovelDetail'),
    url(r'^type/(?P<noveltype_id>[0-9]{1,2})+$',views.NovelTypeList,name='NovelTypeList'),
    url(r'^NovelComment/$',views.NovelComment,name='NovelComment'),
    url(r'^collect/$',views.novelCollect,name='novelCollect'),
    ]
