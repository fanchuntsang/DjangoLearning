from .models import NovelType,Novel,NovelChapter
from django.contrib import admin

@admin.register(NovelType)
class NovelTypeAdmin(admin.ModelAdmin):
    list_display = ['noveltype_id','noveltype_name']
    search_fields = ['noveltype_id','noveltype_name']

@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    list_display = ['novel_id','novel_name']
    search_fields = ['novel_id','novel_name','novel_type','novel_author','novel_state']
    ordering = ['novel_id']

@admin.register(NovelChapter)
class NovelChapterAdmin(admin.ModelAdmin):
    list_display = ['nchapter_id','novel_id','nchapter_name']
    search_fields = ['nchapter_id','nchapter_name']
    ordering = ['nchapter_id']
