from datetime import datetime

from django.db import models

# Create your models here.
from django.utils.html import format_html


class NovelType(models.Model):
    noveltype_id = models.AutoField(primary_key=True)
    noveltype_name = models.CharField(max_length=5)
    def __str__(self):
        return self.noveltype_name
class Novel(models.Model):
    novel_id = models.AutoField(primary_key=True)
    novel_name = models.CharField(max_length=20,blank=False)
    novel_type = models.ForeignKey('NovelType',on_delete=models.CASCADE)
    novel_author = models.CharField(max_length=5,blank=False)
    novel_state = models.BooleanField(blank=False)
    novel_brief = models.TextField(blank=True)
    novel_pic = models.ImageField(upload_to='pictures/novel_pic/%Y/%m/%d/')
    novel_collectnum = models.IntegerField()
    novel_grade = models.IntegerField()
    def image_data(self):
        return format_html(
            '<img src="{}" width="100px"/>',
            self.image.url,
        )
    image_data.short_description = u'图片'
    def __str__(self):
        return self.novel_name

class NovelChapter(models.Model):
    nchapter_id = models.AutoField(primary_key=True)
    novel = models.ForeignKey('Novel',on_delete=models.CASCADE,default="")
    nchapter_name = models.CharField(max_length=15,blank=False)
    nchapter_content = models.TextField(default="")
    nchapter_updatetime = models.DateField(auto_now=True)
    def __str__(self):
        return self.nchapter_name


