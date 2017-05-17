#coding=utf-8
from django.shortcuts import render,get_object_or_404 
from .models import Article,Category
from django.http import Http404
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
import markdown
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
	article_list = Article.objects.all()
	paginator = Paginator(article_list, 1)
	page = request.GET.get('page')
	try:
		article_list = paginator.page(page)
	except PageNotAnInteger:
		article_list = paginator.page(1)
	except EmptyPage:
		article_list = paginator.page(paginator.num_pages)
	context = {'article_list':article_list} 
	return render(request,'blog/index.html',context)
"""
#博客首页
def index(request):
	try:
		article_list = Article.objects.all()
	except Article.DoesNotExist:
		raise Http404
	context = {'article_list':article_list}
	return render(request,'blog/index.html',context)
"""
#文章详情页面
"""
根据我们从url捕获的文章id
也就是pk，pk意为主键，这里的主键就是id获取我们的article
"""
def detail(request,pk):
	article = get_object_or_404(Article,pk=pk)
	#调用阅读量统计函数
	article.count_views()
	article.body = markdown.markdown(article.body,
			                        extensions=[
								        'markdown.extensions.extra',																			'markdown.extensions.codehilite',															            'markdown.extensions.toc',																				])
	context = {'article':article}
	return render(request,'blog/detail.html',context)
#右侧归档列表
def archives(request,year,month):
	try:
		article_list = Article.objects.filter(created_time__year=year,created_time__month=month)
	except Article.DoesNotExist:
		raise Http404
	paginator = Paginator(article_list, 1)
	page = request.GET.get('page')
	try:
		article_list = paginator.page(page)
	except PageNotAnInteger:
		article_list = paginator.page(1)
	except EmptyPage:
		article_list = paginator.page(paginator.num_pages)
	context = {'article_list':article_list}
	return render(request,'blog/index.html',context)
#右侧分类列表
def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	article_list = Article.objects.filter(category=cate)
	context = {'article_list':article_list}
	paginator = Paginator(article_list, 1)
	page = request.GET.get('page')
	try:
		article_list = paginator.page(page)
	except PageNotAnInteger:
		article_list = paginator.page(1)
	except EmptyPage:
		article_list = paginator.page(paginator.num_pages)
	context = {'article_list':article_list}
	return render(request, 'blog/index.html',context)
#About关于我页面
def about(request):
	context = {}
	return render(request,'blog/about.html',context)
#contact联系我页面
def contact(request):
	context = {}
	return render(request,'blog/contact.html',context)
