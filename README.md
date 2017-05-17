**关于我：**  
Life is short,I use Python!  
Author：zhiyinyouzhao  
Email：5251870@qq.com  
Date：May 17,2017  
**项目说明：**  
基于 django 1.10 ，Python 2.7 ，Mysql5.7和Bootstrap3的个人博客。    
**博客演示地址：**    
**安装说明：**   
1.克隆项目到本地
首先进入保存项目的目录下，输入如下命令：
```python
git clone https://github.com/zhiyinyouzhao/django_blog.git
```
2.安装项目依赖包
进入项目所在django_blog文件夹下，输入如下命令：
```python
sudo pip install -r requirements
```
3.数据库的迁移
确保Mysql数据库安装设置正确，然后再在blogproject目录下，也就是mange.py文件同级目录下，输入如下命令：
```python
python manage.py makemigrations
python manage.py migrate
```
4.创建超级用户
超级用户是我们在后台Admin发布，修改博客文章的用户，命令如下：
```python
python manage.py createsuperuser
```
5.打开开发服务器
```python
python manage.py runserver
```
在浏览器输入网址127.0.0.1:8000/blog/index/。    
默认开发服务器是本地机器的8000端口，你也可以修改例如：    
python manage.py runserver 192.168.1.7:8088    
6.进入后台发布文章    
浏览器输入：http://127.0.0.1:8000/admin/    
**个人小结：**    
1.博客前端来源于[Bootstrap](http://www.bootcss.com/) , 可以去搜索开源的自己喜欢的模板加以修改。    
2.目前未添加评论功能，分页也需要改善，数据库的Tag表也没有使用。   
3.支持Markdown，但是语法高亮只有一种颜色，原因未知。   
**致谢：**    
在博客开发过程中查阅了大量资料，参考了[追梦人物的博客教程](http://zmrenwu.com/)。    
他的教程清晰明了，推荐阅读，再次感谢。
