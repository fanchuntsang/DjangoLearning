from django.conf.urls import url
from . import views
app_name = 'comic'
urlpatterns = [
    url(r'^index/$',views.ComicIndex,name='ComicIndex'),
    url(r'^$',views.ComicIndex,name='ComicIndex'),
    url(r'^detail/(?P<comic_id>[0-9]{1,2})+$',views.ComicDetail,name='ComicDetail'),
    url(r'^type/(?P<comictype_id>[0-9]{1,2})+$',views.ComicTypeList,name='ComicTypeList'),
    url(r'^ComicComment/$',views.ComicComment,name='ComicComment'),
    url(r'^collect/$',views.comicCollect,name='comicCollect'),
    ]
