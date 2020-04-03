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
- 创建虚拟环境
    - conda create -n env_name python=3.6
- 激活conda的虚拟环境
    - (win)conda activate env_name  
           conda activate slm # 
- 安装django：
    - pip install django==2.1.8
    - conda install django==2.1.8（推荐）

    
# 后台需要的流程

#### 创建第一个django项目
   **django-admin startproject tulingxueyuan**
    
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
    - 创建命令：**python manage.py startapp teacher**
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
# 4. URL在app中处理
   - 如果所有应用URL都集中在tulingxueyuan/urls.py中可能导致文件臃肿
    - 可以把urls具体功能追歼分散到每个app中
        - 从django.conf.urls 导入include
        - 注意此时RE部分的写法
        - 添加include导入
    - 使用方法：
        - 确保include被导入
        - 写主路由的开头url
        - 写子路由
        - 编写views函数
    - 同样可以使用参数
# 5. URL中的嵌套参数
   - 捕获某个参数的一部分
        - 例如URL /index/page-3,需要捕获数字3作为参数
        '''
        url(r'index_1/(page-(\d+)/)?$', views.myindex_1), # 不太好
        url(r'index_2/(?:page-(?P<page_number>\d+)/)$',views.myindex_2) # 好
        '''
        - 上述例子会得到两个参数，但?：表名忽略此参数
# 6. 传递额外参数
   - 参数不仅仅来自URL，还可能是我们自己定义的内容
   '''
   url(r'extrem/$',views.extremParam, {'name':"liuying"} ), 
   ''' 
    - 附加参数同样适用于include语句，此时对include内所有都添加 
    
# 7. URL的反向解析
   - 防止硬编码
   - 本质上是对每一个URL进行命名
   - 以后再编码代码中使用URL的值，原则上都应该使用反向解析
   
######  views 视图
# 1. 视图概述
   - 视图即视图函数，接收web请求并返回web响应的事务处理函数。
   - 响应指符合http协议要求的任何内容，包括json，string，html等
   - 本章忽略事务处理，重点在如何返回处理结果上
# 2. 其他简单视图
   - django.http给我们提供了很多和HttpResponse类似的简单视图，
   通过查看django.http代码我们会知道
   - 此类视图使用方法基本类似，可以通过return语句直接返回给浏览器
   -Http404为Exception子类，所以需要raise使用 
 
# 3. HttpResponse详解
- 方法
    - init： 使用页面实例化HttpResponse对象
    - write(content): 以文件的方式写
    - flush(): 以文件的方式输出缓冲区
    - set_cookie(key, value='', max_age=None, expires=None): 设置cookie
        - key,value都是字符串类型
        - max_age是一个整数，表示在指定秒数后过期
        - expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期
        - max-age与expires二选一
        - 如果不指定过期时间，则两个星期后过期
    - delete_cookie(key): 删除指定的key的Cookie，如果key不存在则什么也不发生
    
   备注：cookie放用户电脑上的，不安全，最好不放任何信息
        session放在服务器上, 信息放在session相对安全

# 4. HttpResponseRedirect
   - 重定向，服务器端跳转
   - 构造函数的第一个参数用来指重定向的地址
   - 案例 ShowViews/views.py
        """python
        # 在east/urls/中添加一下内容
        url(r'^v10_1/', views.v10_1),
        url(r'^v10_2/', views.v10_2),
        url(r'^v11/', views.v11, name = "v11"),
        """python
        # /ease/ShowViews/views中添加一下内容
        def v10_1(request):
            return HttpResponseRedirect("/v11")
            
        def v10_2(request):
            return HttpResponseRedirect(reverse("/v11"))  
            
        def v11(request):
            return HttpResponse("哈哈，这是V11的访问返回呀")      

# 5. Request对象
   - Request介绍
        - 服务器接收到http协议的请求后，会根据报文创建HttpRequest对象
        - 视图函数的第一个参数是HttpRequest对象
        - 在django.http模块中定义了HttpRequest对象的API
   - 属性
        - 下面除非特别说明，属性都是只读的
        - path： 一个字符串，表示请求的页面的完整路径，不包含域名
        - method：一个字符串，表示请求使用的HTTP方法，常用值包括：get
        - encoding: 一个字符串，表示提交的数据的编码方式
            - 如果为None则表示使用浏览器的默认设置，一般为utf-8
            - 这个属性时可写的，可以通过修改它来修改访问表单数据使用的编码
        GET: 一个类似于字典的对象，包含get请求方式的所有参数
        POST：一个类似于字典的对象，包含post请求方式的所有参数
        FILES：一个类似于字典的对象，包含所有的上传文件
        COOKIES: 一个标准的Python字典，包含所有的cookie，键和值都为字符串
        session: 一个既可读有可写的类似于字典的对象，表示当前的会话
             - 只有当Django启用会话的支持时才可用
             - 详细内容见“状态保持”
    - 方法：
        - is_ajax(): 如果请求是通过XMLHttpRequest发起的，则返回True
    - QueryDict对象
        - 定义在django.http.QueryDict
        - request对象的属性GET、POST都是QueryDict类型的对象
        - 与Python字典不同，QueryDict类型的对象用来处理同一个键带。。。
        - 方法get(): 根据键获取值
            - 只能获取键的一个值
            - 如果一个键同时拥有多个值，获取最后一个值
        - 方法getlist(): 根据键获取值
            - 将键的值以列表返回，可以获取一个键的多个值
    - Get属性
        - QueryDict类型的对象
        - 包含get请求方式的所有参数
        - 与url请求地址中的参数对应，位于？后面
        - 参数的格式是键值对，如key1 = value1 
        - 多个参数之间，使用&连接， 如key1 = value1
        - 键是开发人员定下来的，值是可变的
        - 案例ShowViews/views/v8_get
        
     - POST属性
        - QueryDict类型的对象
        - 包含post请求方式的所有参数
        - 与form表单中的控件对应
        - 表单中空间必须有name属性，name为键，value为值
            **- checkbox存在一键多值的问题**
        - 键是开发人员定下来的，值是可变的
        - 案例ShowViews/views/v9_post
            - settings中设置模板位置(已经设置完毕)
            - 设置get页面的urls和函数
            """python
            # east/urls.py
            # 需要在路由文件中添加两个路由
            url(r'^v9_get/', views.v9_get),
            url(r'^v9_post/', views.v9_post),
            """python
            
            # ShowViews/views.py
            # 在文件中添加下面两个处理函数
            def v9_get(request):
                return render_to_response("for_post.html")
                
            def v9_post(request):
                rst = ""
                for k,v in request.POST.items():
                    rst += k + "-->" + v
                    rst += ","
                    newrst = rst.strip(",")
                    
                return HttpResponse("{}".format(newrst))
                
       #### 备注：
        # 1. 在setting中MIDDLEWARE中将CSRF的防护禁止掉，就不会出现forbidden 403
            # 'django.middleware.csrf.CsrfViewMiddleware'
        # 2. 在setting中添加模板路径
            #  'DIRS': [os.path.join(BASE_DIR, "templates")]
      
### 6 手动编写视图
   - 实验目的
        - 利用django快捷函数手动编写视图处理函数
        - 编写过程中理解视图运行原理
    - 分析：
        - django把所有请求信息封装如request
        - django通过urls摸摸看把相应请求跟事件处理函数连接起来，并把request作为参数传入
        - 在相应的处理函数中，我们需要完成两部分
            - 处理业务
            - 把结果封装并返回，我们可以使用简单HttpResponse，同样也
        - 本案例不介绍业务处理，把目光集中在如何渲染结果

     - render：
        - render(request, template_name[, context][, context_instance])
            - 使用模板和一个给定的上下文环境，返回一个渲染和HttpResponse
            - request:django的传入请求
            - template_name:模板名称
            - context_instance: 上下文环境
            - 案例参看代码 teacher_app/views/render_test
    - render_to_response
    备注： render是render_to_response的升级版，常用render
           视图返回的必须是Response子类，不能是其他的类
           
## 7.系统内建视图
   -  系统内建视图，可以直接使用
    - 404
        - defaults.page_not_found(request, template_name = '404.html')
        - 系统引发Http404时触发
        - 默认request_path变量给模板，即导致错误的URL
        **- DEBUG=True则不会调用404，取而代之的是调试信息**
        - 404视图会被传递一个RequestContext对象并且可以访问模板上下文处理器提供的变量
        
   - 500(server error)
        - defaults.server_error(request, template_name = '500.html')
        - 需要DEBUG=False,否则不调用
    - 403(Http Forbidden)视图
        - defaults.permission_denied(request, template_name= '403.html')
        - 通过PermissionDenied触发
    - 400（bad request）视图
        - defaults.bad_request(request, template_name = '400.html')
        - DEBUG= False
       
## 8. 基于类的视图
   - 和基于函数的视图的有事与区别：
        - HTTP 方法的methode可以由各自的方法，不需要使用条件分支来解决
        - 可以使用OOP技术（例如Mixin）
    - 概述
        - 核心是允许使用不同实例方法来响应不同的HTTP请求方法，而避开条件分支实现
        - as_view函数作为类的可调用入库，该方法擦黄健一个实例并调用dispatch方法，按照请求方法
        
   - 类属性使用
         - 在类定义时直接覆盖
         - 在调用as_view的时候直接最为参数使用，例如：
         '''urlpatterns = [
         url(r'^about/',GreetingView.as_view)
         ]'''  
    - 对于类的视图的扩充大致有三种方法：Mixin，装饰as_view, 装饰dispatch
    - 使用Mixin
        - 多继承的一种形式，来自父类的行为和属性组合在一起
        - 解决多继承问题
        - View的子类只能单继承，多继承会导致不可期问题
        - 多继承带来的问题：
            - 结构复杂
            - 优先顺序模糊
            - 功能冲突
        - 解决方法
            - 规格继承 - java interface
            - 实现继承 - python,ruby
      - 在URLconf中装饰
            from django.contrib.auto.decorators import login_required, permission_required
            from django.views.generic import TemplateView
            
            from .view import VoteView
            
            urlpatterns = [
                url(r'^about/', login_required(TemplateView.as_view(template)))
                url(r'^vote/', permission_required('polls.can_vote')(Voteview))
            ]
            
## 9 模型models （**转接口**）
    -  可以在类中的实例 通过转接口获得数据，不与数据库打交道
   - ORM
        - ObjectRelationMap: 把面向对象思想转换成关系数据库
        - 类对应表格
        - 类中的属性对应表中的字段
        - 在应用中的models.py文件中定义class
        - 所有需要使用ORM的class都必须是models.Model的子类
        - class中的所有属性对应表格中的字段
        - 字段的类型必须使用models.xxx 不能使用python中的类型
        - 在django中，Models负责跟数据库交互    
    - django连接数据库
         - 自带默认数据库slqlite3
            - 关系型数据库
            - 轻量级
         - 建议开发用sqlite3,部署用mysql之类的数据库
         - **切换数据库在setting中进行配置数据库代码：**
            # django连接mysql
             DATABASES = [
                'default' = {
                    'ENGINE' : 'django.db.backends.mysql',
                    'NAME' :'数据库名',
                    'PASSWORD': '数据库密码',
                    'HOST' : '127.0.0.1',
                    'PORT' : '3306',
                }
             ]
         - 需要在项目文件下的__init__文件中导入pymysql包
         
             import pymysql
             pymysql.install_as_MySQLdb()
         
# models类的使用
   - 定义和数据库表映射的类
        - 在应用中的models.py文件中定义class
        - 所有需要使用ORM的class都必须是models.Model的子类       
        - 类中的所有属性对应表中的字段
        - 字段的类型必须使用models.xxx 不能使用python中类型
    - 字段常用参数
        - 1. max_length: 规定数值的最大长度
        - 2. blank: 是否允许字段为空，默认不允许
        - 3. null: 在DB中控制是否保存为null，默认为false
        - 4. default: 默认值
        - 5. unique: 唯一
        - 6. verbose_name: 假名
    - 数据库的迁移
        - 1. 在命令行中，生成数据迁移的数据(生成sql语句)
                
                python manage.py makemigrations
        
        - 2. 在命令行中，输入数据迁移的指令
                
                python manage.py migrate
                
               ps: 如果迁移中出现没有变化或者报错，可以尝试强制迁移
               
               # 强制迁移命令
                - python manage.py makemigrations 应用名
                - python manage.py migrate 应用名
         - 3. 对于默认数据库，为了避免出现混乱，如果数据库中没有数据，每次迁移前可以把
         自带的sqlite3数据库删除
     
******ORM--(Object Relational Mapping)关系对象映射******     
# ### 查看数据库数据
    
   1. 启动命令行： python manage.py shell
    ps:对ORM的操作分为静态函数和非静态函数，两种，静态是指在内存中只有一份，非静态数据每个实例存一份
    2. 在命令行中导入对应的映射类
        from 应用.models import 类名
        - from teacher.models import Teacher
    3. 使用objects属性操作数据库. **objects是模型中实际与数据库交互的**
    4. 查询命令
        - 类名.objects.all() 查询数据库表中所有内容，返回结果是一个Query
            - Teacher.objects.all()
        - 类名.object.filter(条件) 
            - Teacher.objects.filter(age=18)  查询年龄是18岁的人
        
      5. 插入命令
        dana = Teacher()  # 创建一个类的实例
        dana.nama = "Dana"  # 给对象的属性赋值
        dana.age = 18
        dana.address = "tulingxueyuan"
        
        dana.save()  # 将所有保存到数据库中
        
        # 遍历
        ta = Teacher.objects.all()
        for t in ta：
            print("Name:{0}, age:{1}, Address:{2}, Course:{3}".format(t.name, t.age, t.address, t.course))
   
   - 常见查找方法
    1. 通用查找格式：属性名 _ _ (用下面的内容) = 值exit
    
        - gt : 大于   例如：ta = Teacher.objects.filter(age__gt=18) # 查找年龄大于18岁的
        - gte ：大于等于
        - lt : 小于
        - lte: 小于等于
        - range: 范围
        - year: 年份
        - isnull: 是否为空
     2. 查找等于指定值得格式：属性名 = 值  age =18
     3. 模糊查找： 属性名_ _(使用下面的内容) = 值
     
     * exact ： 精确等于
     * iexact： 不区分大小写
     * contains: 包含     ta = Teacher.objects.filter(course__contains="")
     * startwith: 以...开头
     * endwith: 以...结尾
     
# 模型-数据库表关系   
- 多表联查：利用多个表联合查找某一项信息或多项信息。    
- school:manager 1:1 OneToOne
    - 建立关系：在模型任意一边即可
    - add: 
       - 添加没有关系的一边，直接实例化保存就可以                    
            >>>s = School()
            >>> s.school_id=1
            >>> s.school_name="tulingxueyuan"
            >>> s.save()
            >>> ss = School.objects.all()
            >>> ss
            <QuerySet [<School: nanjingtulingxueyuan>, <School: tulingxueyuan>]>
       - 添加有关系的一边,使用使用实例化或者使用create方法,**建议使用create**
            1. 使用实例化方法：
                >>> m = Manager()
                >>> m.manager_id = 10
                >>> m.manager_name = "dana"
                >>> m.my_school = s
                >>> m.save()
                >>> mm = Manager.objects.all()
                >>> mm
                <QuerySet [<Manager: dana>]>
            2. 使用create方法：
                >>>m = Manager.objects.create(manager_id = 20, manager_name = "erna", my_school=ss[0])
        - Query(查询):
            - 有子表查母表  查询dana校长是哪个学校的
                >>>Manager.objects.get(manager_name="dana").my_school.school_name
            - 有母表查子表  查询叫大拿的学校
                >>>School.objects.get(manager__manager_name="dana")
        - change(修改)
            - 单个修改用save()
            - 批量修改使用update()
                >>> ss = School.objects.all()
                >>> ss.update(school_name="图灵学院")
            - 无论对子表还是母表的修改
        - delete(删除)：直接使用delete删除

- school:teacher 1:N OneToMany
    - 建立关系：
        - 一个表格的一个数据项、对象等，可以有很多个另一个表格的数据项
        - 比如：一个学校可以有很多个老师，但一个老师只有一个学校
        - 在多的一边使用ForeignKey
    - Add(添加)
        - 与一对一的方法类似，通过create和new来添加
            1. 使用实例,需要手动save
                >>> ss = School.objects.all()
                >>> ss
                <QuerySet [<School: nanjingtulingxueyuan>, <School: tulingxueyuan>]>
                >>> ss[0]
                <School: nanjingtulingxueyuan>
                >>> t1 = Teacher()
                >>> t1
                <Teacher: >
                >>> t1.teacher_name = "张三"
                >>> t1.my_school = ss[0]s
                >>> t1.save()
                >>> ts = Teacher.objects.all()
                >>> ts
                <QuerySet [<Teacher: 张三>]>
            2. 使用create方法（推荐）
                >>>t = Teacher.objects.create(teacher_name= "李四", my_school = ss[1])
                >>> t
                <Teacher: 李四>
                >>> ts
                <QuerySet [<Teacher: 张三>, <Teacher: 李四>]>
        - create: 把属性都填满，然后不需要手动保存
        - new: 可以属性或参数为空，必须save保存
    - Query(查找)：
        - 以学校和老师的例子为准
        - 如果知道老师查学校， 则通过增加的关系属性，直接使用
        - 例如：查找t1老师是哪个学校的 
            >>>t1.my_schools
        - 反查：查询学校的所有老师，则需要在老师模型名称的小写下直接加下划线set：teacher_set
            """一对多的关系系统默认添加一个多的一边的属性"""  # teacher_set
            >>>s1.teacher_set.all()
- teacher:student N:N  ManyToMany
    - 表示任意一个表的数据可以拥有对方表格多项数据，反之亦然
    - 比如典型例子：老师和学生的关系
    - 使用上，在任意一方，使用ManyToMany定义，只需要定义一边
    -Add(添加):
        - 添加老师，则使用student.teachers.add()
        >>>tt = Teacher.objects.all()
        <QuerySet [<Teacher: 张三>, <Teacher: 李四>]>
        >>>stu = Student()
        >>>stu.teachers.add(tt[0])
        >>>stu.teachers.all()
        <QuerySet [<Teacher: 张三>]>
        >>>stu.teachers.add(tt[1])
        >>>stu.teachers.all()
        <QuerySet [<Teacher: 张三>, <Teacher: 李四>]>
                
    - Query(查询)
        - 跟一对多一样，使用_set
        - 查找学生对应的所有老师 ss[0].teachers.all()
        - 查找老师对应的所有学生 tt[0].student_set.all()
        >>> tt = Teacher.objects.all()
        >>> tt
        <QuerySet [<Teacher: 张三>, <Teacher: 李四>]>
        >>> ss = Student.objects.all()
        >>> ss
        <QuerySet [<Student: 学生1>]>
        >>> tt[0].student_set
        <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object
         at 0x0000000003D56860>
        >>> tt[0].student_set.all()
        <QuerySet [<Student: 学生1>]>
        >>> ss[0].teachers
        <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object
         at 0x0000000003D56860>
        >>> ss[0].teachers.all()
        <QuerySet [<Teacher: 张三>, <Teacher: 李四>]>
        
# 模板 Template(html/css...)
- 模板：一组相同或者相似的页面，在需要个性化的地方进行留白，需要的时候只需要用数据填充就可以了
- 步骤：
    1. 在settings中进行设置；
        - TEMPLATES
    2. 在templates文件夹下编写模板并调用
    

# 模板-变量
- 变量的表示方法：{{var_name}}  
- 系统调用模板的时候，会用相应的数据查找相应的变量名称，如果能找到则填充或者叫渲染，找不到则跳过；
    # C = dict()
    # C["name"] = "sunlimin"
    >>>render(request, 'two.html', context={"name":"sunlimin"})
- 案例two.html

# 模板-标签
- for标签：{%for .. in ..%}  {% endfor %}
   
    {%for s in score %}
        {{s}}
    {% endfor %}
# if标签
- 用来判断条件
- 代码示例：
    {%if 条件 %}
        条件成立执行语句
    {% elif 条件 %}
        条件成立执行语句
    {% else %}
        以上条件不成立执行语句
    {% endif %}
    
    {% if name == "王晓静" %}
        {{name}},你好
    {% elif name == "张晓静" %}
        {{name}},hello
    {% endif %}
# csrf标签
- csrf:跨站请求伪造
- 在提交表单的时候，表单页面需要加上{% csrf_token%},
- 案例 five_get,five_post
   
   

        
        