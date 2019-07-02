from django.contrib import admin
from .models import Collect

# Register your models here.
@admin.register(Collect)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_id','collect_type','collect_in_id']
    search_fields = ['comment_id','comment_type','user_id','comment_content']
