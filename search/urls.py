from django.conf.urls import url
app_name = 'search'

from . import views

urlpatterns = [
    url(r'^$',views.search_qidian,name='search_qidian'),
]
