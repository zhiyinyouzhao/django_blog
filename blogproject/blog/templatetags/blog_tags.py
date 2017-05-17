#coding=utf-8
from ..models import Article,Category
from django import template
from django.utils.safestring import mark_safe
#实例化一个template.Library
register = template.Library()
#近期文章，获得数据库中前num篇文章
@register.assignment_tag
def get_recent_articles():
	return Article.objects.all()
#归档
@register.assignment_tag
def archives():
	#通过dates返回列表，精确到月，降序排列。
	return Article.objects.datetimes('created_time','month',order='DESC',tzinfo=None)
#分类
@register.assignment_tag
def get_categories():
	return Category.objects.all()
