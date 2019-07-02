from django.contrib import admin
from .models import Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_id','user_id','comment_content']
    search_fields = ['comment_id','comment_type','user_id','comment_content']
