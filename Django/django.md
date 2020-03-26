# Django系统

- 环境
    - python 3.6
    - django 2.x
参考资料：
[django中文教程]https://yiyibooks.cn  一译
django架站的16堂课

# 环境搭建
- anaconda+pycharm
- anaconda使用
    - conda list:显示当前环境安装的包
    - conda env list:显示安装的虚拟环境
    - conda create -n env_name python=3.6
- 激活conda的虚拟环境
    - (win)conda activate env_name  
           conda activate slm # 
- 安装django：
    - pip install django==2.1.4
    - conda install django==2.1.4（推荐）

    
# 后台需要的流程

#### 创建第一个django项目
   django-admin startproject tulingxueyuan
    
manage:负责命令行参数处理
settings:配置文件
urls:和路由相关代码
wsgi:通用网关

#### 启动django
1。命令行启动：python manage.py runserver 
    django2.2启动失败有bug，django2.1.4正常启动
2. Pycharm启动：
    需要配置： 在Edit Configuration 添加 参数 runserver

备注：启动运行http://127.0.0.1:8000/

自动生成db.sqlite3,django自带的数据库

# 路由系统-urls
- 创建app
    - app: 负责一个具体业务或者一类具体业务模块
    - 创建命令：python manage.py startapp teacher
admin.py:
apps.py:
models.py:
tests.py:
views.py: 视图文件 视图函数在urls中在调用，视图函数需要一个参数，类型应该是HttpRequest

- 路由：（相当于一个中间件，中枢）
    - 按照具体的请求url，导入到相应业务处理模块的一个功能
    - 是django的信息控制中枢，通过路由能找到各个请求路口
    - 本质上是接收URL和相应的处理模块的一个映射
    - 在接受URL请求的匹配上使用RE（django2.0+之后不用正则了 用url代替re_path）
    - URL的具体格式urls.py中所示
    
- 需要关注两点：
    1. 接收的URL是什么
    2. 已知URL匹配到哪个处理模块
    
- django怎么处理请求：
    - 一旦生成url页面请求，请求传递到urls.py
    - django去urlpatterns中匹配链接（Django会在匹配到的第一个就停下来）
    - 一旦匹配成功，就会去执行，path后面的方法，Django便会给出相应的view页面
    （该页面可以为一个Python的函数，或者基于view（Django内置的）的类），也就是用户看到的页面
    - 自上而下若匹配失败，则出现错误的页面


# 2 正常映射
- 把某一个符合RE的URL映射达到事务处理函数中
    举例如下：
        
        from showeast import view
        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^normalmap', view.normalmap),
        ]
# 3. URL中带参数映射
    - 在实践处理代码中需要由URL传入参数，形如 /myurl/param中的param
    - 参数都是字符串形式，如果需要整数形式需要强制转换
    - 通常的形式如下：
        /search/page/432中的432需要经常性变换
                