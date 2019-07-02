from django.contrib import admin
from .models import Comic,ComicChapter,ComicType

# Register your models here.
@admin.register(ComicType)
class ComicTypeAdmin(admin.ModelAdmin):
    list_display = ['comictype_id','comictype_name']
    search_fields = ['comictype_id','comictype_name']

@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ['comic_id','comic_name']
    search_fields = ['comic_id','comic_name','comic_author','comic_type','comic_state']
    ordering = ['comic_id']

@admin.register(ComicChapter)
class ComicChapterAdmin(admin.ModelAdmin):
    list_display = ['cchapter_id','comic','cchapter_name']
    search_fields = ['comic']
