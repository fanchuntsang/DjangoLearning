from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class News(models.Model):
    news_id = models.AutoField('序号',primary_key=True)
    news_title = models.CharField('标题',max_length=20)
    news_author = models.CharField('作者',max_length=10)
    news_briefr = models.CharField('简介',max_length=20)
    # news_content = tinymce.models.HTMLField(verbose_name='资讯详情',default="")\
    news_content = RichTextUploadingField(default="")
    news_uploaddate = models.DateTimeField('上传时间',auto_now=True)
    news_clickNum = models.IntegerField('点击量',default=0)
    def __str__(self):
        return self.news_title
