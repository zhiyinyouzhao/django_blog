#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.core.urlresolvers import reverse
# Create your models here.

@python_2_unicode_compatible
## python_2_unicode_compatible 装饰器用于兼容 Python2
class Category(models.Model):
	"""
	django 必须要继承models.Model类
	Category分类表只有一个字段name
	CharField指定了name的类型，是字符型
	max_length是最大长度
	"""
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Tag(models.Model):
	#同分类表
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Article(models.Model):
	#标题
	title = models.CharField(max_length=100)
	#正文，正文使用TextField,因为正文比较长
	body = models.TextField()
	#文章创建时间
	created_time = models.DateTimeField()
	#文章修改时间
	modified_time = models.DateTimeField()
	#文章摘要，可以没有摘要，但是默认情况必须存入数据。
	#否则会报错，指定blank = True，可以存入空值。
	abstract = models.CharField(max_length=200,blank=True)
	"""
	分类与标签，在这里把文章表，分类表和标签表关联起来
	我们规定一篇文章只有一个分类，但是一个分类下可以有多篇文章。
	所以是一对多的关系，所以使用外键。而对于标签来说，一篇文章可以有多个标签，同一个标签下也可以有多个文章，这是多对多的关系，我们使用ManyToManyField。同时我们规定文章可以没有标签，因此为标签tags指定了blank=True。
	"""
	#分类
	category = models.ForeignKey(Category)
	#标签
	tags = models.ManyToManyField(Tag,blank=True)
	#文章作者
	"""
	这里的User是从django.contrib.auth.models导入的
	django.contrib.auth是django内置的应用。
	专门用于处理网站用户的注册，登录等流程，
	User是django写好的用户模型，
	我们通过Foreginkey,把文章和User关联起来，
	我们规范一篇文章只能有一个作者，而一个作者可以写多篇文章，
	因此这是一对多的关系.
	"""
	author = models.ForeignKey(User)
	#文章阅读数量,PositiveIntegerField该类型的值只允许为正整数或 0，
	#毕竟阅读量不可能为负值。初始化时 views 的值为 0.
	views = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.title
	#自定义get_absolute_url 方法
	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'pk': self.pk})
	#自定义统计阅读量方法
	"""
	increase_views 方法首先将自身对应的 views 字段的值 +1（此时数据库中的值还没变）.
	然后调用 save 方法将更改后的值保存到数据库。
	注意这里使用了 update_fields 参数来告诉 Django 只更新数据库中 views 字段的值，以提高效率。
	"""
	def count_views(self):
		self.views += 1
		self.save(update_fields=['views'])
	
	"""
	django 允许我们在 models.Model 的子类里定义一个 Meta 的内部类，
	这个内部类通过指定一些属性来规定这个类本该有的一些特性，例如在这里我们要指定 Post 的排序方式。
	这里 ordering 属性用来指定文章排序方式，['-created_time'] 指定了依据哪个属性的值进行排序，
	这里指定了文章发布时间，且负号表示逆序排列。
	这里列表中可以用多个项，比如 ordering = ['-created_time', 'title'] ，
	那么首先会依据 created_time 排序，如果 created_time 的值相同，则再依据 title 排序。
	"""
	class Meta:
		ordering = ['-created_time','title']
