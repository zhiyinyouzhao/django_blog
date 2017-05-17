#coding=utf-8
from django.contrib import admin
from .models import Article,Category,Tag
import sys
reload(sys)
sys.setdefaultencoding("utf8")

class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
#注册后台模型
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
