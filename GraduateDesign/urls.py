"""GraduateDesign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from django.conf import settings
import xadmin
from django.urls import include
from django.views.static import serve
from GraduateDesign.settings import MEDIA_ROOT

from . import view

xadmin.autodiscover()
app_name = 'GraduateDesign'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', view.hello),
    url(r'^index/', view.hello),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^user/',include('user.urls')),
    url(r'^search/',include('search.urls',namespace='search')),
    url(r'^news/',include('news.urls',namespace='news')),
    url(r'^novel/',include('novel.urls',namespace='novel')),
    url(r'^comic/',include('comic.urls',namespace='comic')),
    url(r'^media/(?P<path>.*)', serve, {"document_root":MEDIA_ROOT}),

]
urlpatterns += static('/upload/', document_root=settings.MEDIA_ROOT)
