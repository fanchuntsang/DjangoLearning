from django.db import models
from django.conf import settings
# Create your models here.


class Collect(models.Model):
    collect_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    collect_type = models.IntegerField(blank=False)
    collect_in_id = models.IntegerField(blank=False,default="1")
    collect_name = models.CharField('标题',max_length=20,default="")
