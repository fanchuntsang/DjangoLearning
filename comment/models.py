from django.db import models
from django.conf import settings
# Create your models here.


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    comment_type = models.IntegerField(blank=False)
    comment_in_id = models.IntegerField(blank=False,default="1")
    comment_content = models.TextField(max_length=140,default="")
