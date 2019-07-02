from django.contrib import admin
from .models import News

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['news_id','news_title','news_author']
    search_fields = ['news_id','news_title']
    ordring = ['id']
