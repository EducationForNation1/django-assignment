from django.contrib import admin
from . models import Message, Comment

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','user','content','created_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','user','message','content','created_at')

admin.site.register(Message,MessageAdmin)
admin.site.register(Comment,CommentAdmin)