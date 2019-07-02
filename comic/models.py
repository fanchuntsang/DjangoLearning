from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.html import format_html
# Create your models here.


class ComicType(models.Model):
    comictype_id = models.AutoField(primary_key=True)
    comictype_name = models.CharField(max_length=5)
    def __str__(self):
        return self.comictype_name

class Comic(models.Model):
    comic_id = models.AutoField(primary_key=True)
    comic_name = models.CharField(max_length=20)
    comic_type = models.ForeignKey('ComicType',on_delete=models.CASCADE)
    comic_state = models.BooleanField(blank=False)
    comic_author = models.CharField(max_length=10)
    comic_brief = models.TextField(blank=True)
    comic_pic = models.ImageField(upload_to='pictures/comic_pic/%Y/%m/%d')
    comic_collectnum = models.IntegerField(blank=False)
    comic_grade = models.IntegerField(blank=False)
    def image_data(self):
        return format_html(
            '<img src="{}" width="100px"/>',
            self.image.url,
        )
    image_data.short_description = u'图片'
    def __str__(self):
        return self.comic_name

class ComicChapter(models.Model):
    cchapter_id = models.AutoField(primary_key=True)
    comic = models.ForeignKey('Comic',on_delete=models.CASCADE,default="")
    cchapter_name = models.CharField(max_length=15,blank=False)
    cchapter_content = RichTextUploadingField(default="")
    cchapter_updatetime = models.DateField(auto_now=True)
    def __str__(self):
        return self.cchapter_name

