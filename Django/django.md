# Djangoϵͳ

- ����
    - python 3.6
    - django 2.x
�ο����ϣ�
[django���Ľ̳�]https://yiyibooks.cn  һ��
django��վ��16�ÿ�

# �����
- anaconda+pycharm
- anacondaʹ��
    - conda list:��ʾ��ǰ������װ�İ�
    - conda env list:��ʾ��װ�����⻷��
- �������⻷��
    - conda create -n env_name python=3.6
- ����conda�����⻷��
    - (win)conda activate env_name  
           conda activate slm # 
- ��װdjango��
    - pip install django==2.1.8
    - conda install django==2.1.8���Ƽ���

    
# ��̨��Ҫ������

#### ������һ��django��Ŀ
   **django-admin startproject tulingxueyuan**
    
manage:���������в�������
settings:�����ļ�
urls:��·����ش���
wsgi:ͨ������

#### ����django
1��������������python manage.py runserver 
    django2.2����ʧ����bug��django2.1.4��������
2. Pycharm������
    ��Ҫ���ã� ��Edit Configuration ��� ���� runserver

��ע����������http://127.0.0.1:8000/

�Զ�����db.sqlite3,django�Դ������ݿ�

# ·��ϵͳ-urls
- ����app
    - app: ����һ������ҵ�����һ�����ҵ��ģ��
    - �������**python manage.py startapp teacher**
admin.py:
apps.py:
models.py:
tests.py:
views.py: ��ͼ�ļ� ��ͼ������urls���ڵ��ã���ͼ������Ҫһ������������Ӧ����HttpRequest

- ·�ɣ����൱��һ���м�������ࣩ
    - ���վ��������url�����뵽��Ӧҵ����ģ���һ������
    - ��django����Ϣ�������࣬ͨ��·�����ҵ���������·��
    - �������ǽ���URL����Ӧ�Ĵ���ģ���һ��ӳ��
    - �ڽ���URL�����ƥ����ʹ��RE��django2.0+֮���������� ��url����re_path��
    - URL�ľ����ʽurls.py����ʾ
    
- ��Ҫ��ע���㣺
    1. ���յ�URL��ʲô
    2. ��֪URLƥ�䵽�ĸ�����ģ��
    
- django��ô��������
    - һ������urlҳ���������󴫵ݵ�urls.py
    - djangoȥurlpatterns��ƥ�����ӣ�Django����ƥ�䵽�ĵ�һ����ͣ������
    - һ��ƥ��ɹ����ͻ�ȥִ�У�path����ķ�����Django��������Ӧ��viewҳ��
    ����ҳ�����Ϊһ��Python�ĺ��������߻���view��Django���õģ����ࣩ��Ҳ�����û�������ҳ��
    - ���϶�����ƥ��ʧ�ܣ�����ִ����ҳ��


# 2 ����ӳ��
- ��ĳһ������RE��URLӳ��ﵽ����������
    �������£�
        
        from showeast import view
        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^normalmap', view.normalmap),
        ]
# 3. URL�д�����ӳ��
   - ��ʵ�������������Ҫ��URL������������� /myurl/param�е�param
    - ���������ַ�����ʽ�������Ҫ������ʽ��Ҫǿ��ת��
    - ͨ������ʽ���£�
        /search/page/432�е�432��Ҫ�����Ա任
# 4. URL��app�д���
   - �������Ӧ��URL��������tulingxueyuan/urls.py�п��ܵ����ļ�ӷ��
    - ���԰�urls���幦��׷�߷�ɢ��ÿ��app��
        - ��django.conf.urls ����include
        - ע���ʱRE���ֵ�д��
        - ���include����
    - ʹ�÷�����
        - ȷ��include������
        - д��·�ɵĿ�ͷurl
        - д��·��
        - ��дviews����
    - ͬ������ʹ�ò���
# 5. URL�е�Ƕ�ײ���
   - ����ĳ��������һ����
        - ����URL /index/page-3,��Ҫ��������3��Ϊ����
        '''
        url(r'index_1/(page-(\d+)/)?$', views.myindex_1), # ��̫��
        url(r'index_2/(?:page-(?P<page_number>\d+)/)$',views.myindex_2) # ��
        '''
        - �������ӻ�õ�������������?���������Դ˲���
# 6. ���ݶ������
   - ��������������URL���������������Լ����������
   '''
   url(r'extrem/$',views.extremParam, {'name':"liuying"} ), 
   ''' 
    - ���Ӳ���ͬ��������include��䣬��ʱ��include�����ж���� 
    
# 7. URL�ķ������
   - ��ֹӲ����
   - �������Ƕ�ÿһ��URL��������
   - �Ժ��ٱ��������ʹ��URL��ֵ��ԭ���϶�Ӧ��ʹ�÷������
   
######  views ��ͼ
# 1. ��ͼ����
   - ��ͼ����ͼ����������web���󲢷���web��Ӧ������������
   - ��Ӧָ����httpЭ��Ҫ����κ����ݣ�����json��string��html��
   - ���º����������ص�����η��ش�������
# 2. ��������ͼ
   - django.http�������ṩ�˺ܶ��HttpResponse���Ƶļ���ͼ��
   ͨ���鿴django.http�������ǻ�֪��
   - ������ͼʹ�÷����������ƣ�����ͨ��return���ֱ�ӷ��ظ������
   -Http404ΪException���࣬������Ҫraiseʹ�� 
 
# 3. HttpResponse���
- ����
    - init�� ʹ��ҳ��ʵ����HttpResponse����
    - write(content): ���ļ��ķ�ʽд
    - flush(): ���ļ��ķ�ʽ���������
    - set_cookie(key, value='', max_age=None, expires=None): ����cookie
        - key,value�����ַ�������
        - max_age��һ����������ʾ��ָ�����������
        - expires��һ��datetime��timedelta���󣬻Ự�������ָ��������/ʱ�����
        - max-age��expires��ѡһ
        - �����ָ������ʱ�䣬���������ں����
    - delete_cookie(key): ɾ��ָ����key��Cookie�����key��������ʲôҲ������
    
   ��ע��cookie���û������ϵģ�����ȫ����ò����κ���Ϣ
        session���ڷ�������, ��Ϣ����session��԰�ȫ

# 4. HttpResponseRedirect
   - �ض��򣬷���������ת
   - ���캯���ĵ�һ����������ָ�ض���ĵ�ַ
   - ���� ShowViews/views.py
        """python
        # ��east/urls/�����һ������
        url(r'^v10_1/', views.v10_1),
        url(r'^v10_2/', views.v10_2),
        url(r'^v11/', views.v11, name = "v11"),
        """python
        # /ease/ShowViews/views�����һ������
        def v10_1(request):
            return HttpResponseRedirect("/v11")
            
        def v10_2(request):
            return HttpResponseRedirect(reverse("/v11"))  
            
        def v11(request):
            return HttpResponse("����������V11�ķ��ʷ���ѽ")      

# 5. Request����
   - Request����
        - ���������յ�httpЭ�������󣬻���ݱ��Ĵ���HttpRequest����
        - ��ͼ�����ĵ�һ��������HttpRequest����
        - ��django.httpģ���ж�����HttpRequest�����API
   - ����
        - ��������ر�˵�������Զ���ֻ����
        - path�� һ���ַ�������ʾ�����ҳ�������·��������������
        - method��һ���ַ�������ʾ����ʹ�õ�HTTP����������ֵ������get
        - encoding: һ���ַ�������ʾ�ύ�����ݵı��뷽ʽ
            - ���ΪNone���ʾʹ���������Ĭ�����ã�һ��Ϊutf-8
            - �������ʱ��д�ģ�����ͨ���޸������޸ķ��ʱ�����ʹ�õı���
        GET: һ���������ֵ�Ķ��󣬰���get����ʽ�����в���
        POST��һ���������ֵ�Ķ��󣬰���post����ʽ�����в���
        FILES��һ���������ֵ�Ķ��󣬰������е��ϴ��ļ�
        COOKIES: һ����׼��Python�ֵ䣬�������е�cookie������ֵ��Ϊ�ַ���
        session: һ���ȿɶ��п�д���������ֵ�Ķ��󣬱�ʾ��ǰ�ĻỰ
             - ֻ�е�Django���ûỰ��֧��ʱ�ſ���
             - ��ϸ���ݼ���״̬���֡�
    - ������
        - is_ajax(): ���������ͨ��XMLHttpRequest����ģ��򷵻�True
    - QueryDict����
        - ������django.http.QueryDict
        - request���������GET��POST����QueryDict���͵Ķ���
        - ��Python�ֵ䲻ͬ��QueryDict���͵Ķ�����������ͬһ������������
        - ����get(): ���ݼ���ȡֵ
            - ֻ�ܻ�ȡ����һ��ֵ
            - ���һ����ͬʱӵ�ж��ֵ����ȡ���һ��ֵ
        - ����getlist(): ���ݼ���ȡֵ
            - ������ֵ���б��أ����Ի�ȡһ�����Ķ��ֵ
    - Get����
        - QueryDict���͵Ķ���
        - ����get����ʽ�����в���
        - ��url�����ַ�еĲ�����Ӧ��λ�ڣ�����
        - �����ĸ�ʽ�Ǽ�ֵ�ԣ���key1 = value1 
        - �������֮�䣬ʹ��&���ӣ� ��key1 = value1
        - ���ǿ�����Ա�������ģ�ֵ�ǿɱ��
        - ����ShowViews/views/v8_get
        
     - POST����
        - QueryDict���͵Ķ���
        - ����post����ʽ�����в���
        - ��form���еĿؼ���Ӧ
        - ���пռ������name���ԣ�nameΪ����valueΪֵ
            **- checkbox����һ����ֵ������**
        - ���ǿ�����Ա�������ģ�ֵ�ǿɱ��
        - ����ShowViews/views/v9_post
            - settings������ģ��λ��(�Ѿ��������)
            - ����getҳ���urls�ͺ���
            """python
            # east/urls.py
            # ��Ҫ��·���ļ����������·��
            url(r'^v9_get/', views.v9_get),
            url(r'^v9_post/', views.v9_post),
            """python
            
            # ShowViews/views.py
            # ���ļ��������������������
            def v9_get(request):
                return render_to_response("for_post.html")
                
            def v9_post(request):
                rst = ""
                for k,v in request.POST.items():
                    rst += k + "-->" + v
                    rst += ","
                    newrst = rst.strip(",")
                    
                return HttpResponse("{}".format(newrst))
                
       #### ��ע��
        # 1. ��setting��MIDDLEWARE�н�CSRF�ķ�����ֹ�����Ͳ������forbidden 403
            # 'django.middleware.csrf.CsrfViewMiddleware'
        # 2. ��setting�����ģ��·��
            #  'DIRS': [os.path.join(BASE_DIR, "templates")]
      
### 6 �ֶ���д��ͼ
   - ʵ��Ŀ��
        - ����django��ݺ����ֶ���д��ͼ������
        - ��д�����������ͼ����ԭ��
    - ������
        - django������������Ϣ��װ��request
        - djangoͨ��urls����������Ӧ������¼���������������������request��Ϊ��������
        - ����Ӧ�Ĵ������У�������Ҫ���������
            - ����ҵ��
            - �ѽ����װ�����أ����ǿ���ʹ�ü�HttpResponse��ͬ��Ҳ
        - ������������ҵ������Ŀ�⼯���������Ⱦ���

     - render��
        - render(request, template_name[, context][, context_instance])
            - ʹ��ģ���һ�������������Ļ���������һ����Ⱦ��HttpResponse
            - request:django�Ĵ�������
            - template_name:ģ������
            - context_instance: �����Ļ���
            - �����ο����� teacher_app/views/render_test
    - render_to_response
    ��ע�� render��render_to_response�������棬����render
           ��ͼ���صı�����Response���࣬��������������
           
## 7.ϵͳ�ڽ���ͼ
   -  ϵͳ�ڽ���ͼ������ֱ��ʹ��
    - 404
        - defaults.page_not_found(request, template_name = '404.html')
        - ϵͳ����Http404ʱ����
        - Ĭ��request_path������ģ�壬�����´����URL
        **- DEBUG=True�򲻻����404��ȡ����֮���ǵ�����Ϣ**
        - 404��ͼ�ᱻ����һ��RequestContext�����ҿ��Է���ģ�������Ĵ������ṩ�ı���
        
   - 500(server error)
        - defaults.server_error(request, template_name = '500.html')
        - ��ҪDEBUG=False,���򲻵���
    - 403(Http Forbidden)��ͼ
        - defaults.permission_denied(request, template_name= '403.html')
        - ͨ��PermissionDenied����
    - 400��bad request����ͼ
        - defaults.bad_request(request, template_name = '400.html')
        - DEBUG= False
       
## 8. ���������ͼ
   - �ͻ��ں�������ͼ������������
        - HTTP ������methode�����ɸ��Եķ���������Ҫʹ��������֧�����
        - ����ʹ��OOP����������Mixin��
    - ����
        - ����������ʹ�ò�ͬʵ����������Ӧ��ͬ��HTTP���󷽷������ܿ�������֧ʵ��
        - as_view������Ϊ��Ŀɵ�����⣬�÷������ƽ�һ��ʵ��������dispatch�������������󷽷�
        
   - ������ʹ��
         - ���ඨ��ʱֱ�Ӹ���
         - �ڵ���as_view��ʱ��ֱ����Ϊ����ʹ�ã����磺
         '''urlpatterns = [
         url(r'^about/',GreetingView.as_view)
         ]'''  
    - ���������ͼ��������������ַ�����Mixin��װ��as_view, װ��dispatch
    - ʹ��Mixin
        - ��̳е�һ����ʽ�����Ը������Ϊ�����������һ��
        - �����̳�����
        - View������ֻ�ܵ��̳У���̳лᵼ�²���������
        - ��̳д��������⣺
            - �ṹ����
            - ����˳��ģ��
            - ���ܳ�ͻ
        - �������
            - ���̳� - java interface
            - ʵ�ּ̳� - python,ruby
      - ��URLconf��װ��
            from django.contrib.auto.decorators import login_required, permission_required
            from django.views.generic import TemplateView
            
            from .view import VoteView
            
            urlpatterns = [
                url(r'^about/', login_required(TemplateView.as_view(template)))
                url(r'^vote/', permission_required('polls.can_vote')(Voteview))
            ]
            
## 9 ģ��models ��**ת�ӿ�**��
    -  ���������е�ʵ�� ͨ��ת�ӿڻ�����ݣ��������ݿ�򽻵�
   - ORM
        - ObjectRelationMap: ���������˼��ת���ɹ�ϵ���ݿ�
        - ���Ӧ���
        - ���е����Զ�Ӧ���е��ֶ�
        - ��Ӧ���е�models.py�ļ��ж���class
        - ������Ҫʹ��ORM��class��������models.Model������
        - class�е��������Զ�Ӧ����е��ֶ�
        - �ֶε����ͱ���ʹ��models.xxx ����ʹ��python�е�����
        - ��django�У�Models��������ݿ⽻��    
    - django�������ݿ�
         - �Դ�Ĭ�����ݿ�slqlite3
            - ��ϵ�����ݿ�
            - ������
         - ���鿪����sqlite3,������mysql֮������ݿ�
         - **�л����ݿ���setting�н����������ݿ���룺**
            # django����mysql
             DATABASES = [
                'default' = {
                    'ENGINE' : 'django.db.backends.mysql',
                    'NAME' :'���ݿ���',
                    'PASSWORD': '���ݿ�����',
                    'HOST' : '127.0.0.1',
                    'PORT' : '3306',
                }
             ]
         - ��Ҫ����Ŀ�ļ��µ�__init__�ļ��е���pymysql��
         
             import pymysql
             pymysql.install_as_MySQLdb()
         
# models���ʹ��
   - ��������ݿ��ӳ�����
        - ��Ӧ���е�models.py�ļ��ж���class
        - ������Ҫʹ��ORM��class��������models.Model������       
        - ���е��������Զ�Ӧ���е��ֶ�
        - �ֶε����ͱ���ʹ��models.xxx ����ʹ��python������
    - �ֶγ��ò���
        - 1. max_length: �涨��ֵ����󳤶�
        - 2. blank: �Ƿ������ֶ�Ϊ�գ�Ĭ�ϲ�����
        - 3. null: ��DB�п����Ƿ񱣴�Ϊnull��Ĭ��Ϊfalse
        - 4. default: Ĭ��ֵ
        - 5. unique: Ψһ
        - 6. verbose_name: ����
    - ���ݿ��Ǩ��
        - 1. ���������У���������Ǩ�Ƶ�����(����sql���)
                
                python manage.py makemigrations
        
        - 2. ���������У���������Ǩ�Ƶ�ָ��
                
                python manage.py migrate
                
               ps: ���Ǩ���г���û�б仯���߱������Գ���ǿ��Ǩ��
               
               # ǿ��Ǩ������
                - python manage.py makemigrations Ӧ����
                - python manage.py migrate Ӧ����
         - 3. ����Ĭ�����ݿ⣬Ϊ�˱�����ֻ��ң�������ݿ���û�����ݣ�ÿ��Ǩ��ǰ���԰�
         �Դ���sqlite3���ݿ�ɾ��
     
******ORM--(Object Relational Mapping)��ϵ����ӳ��******     
# ### �鿴���ݿ�����
    
   1. ���������У� python manage.py shell
    ps:��ORM�Ĳ�����Ϊ��̬�����ͷǾ�̬���������֣���̬��ָ���ڴ���ֻ��һ�ݣ��Ǿ�̬����ÿ��ʵ����һ��
    2. ���������е����Ӧ��ӳ����
        from Ӧ��.models import ����
        - from teacher.models import Teacher
    3. ʹ��objects���Բ������ݿ�. **objects��ģ����ʵ�������ݿ⽻����**
    4. ��ѯ����
        - ����.objects.all() ��ѯ���ݿ�����������ݣ����ؽ����һ��Query
            - Teacher.objects.all()
        - ����.object.filter(����) 
            - Teacher.objects.filter(age=18)  ��ѯ������18�����
        
      5. ��������
        dana = Teacher()  # ����һ�����ʵ��
        dana.nama = "Dana"  # ����������Ը�ֵ
        dana.age = 18
        dana.address = "tulingxueyuan"
        
        dana.save()  # �����б��浽���ݿ���
        
        # ����
        ta = Teacher.objects.all()
        for t in ta��
            print("Name:{0}, age:{1}, Address:{2}, Course:{3}".format(t.name, t.age, t.address, t.course))
   
   - �������ҷ���
    1. ͨ�ò��Ҹ�ʽ�������� _ _ (�����������) = ֵexit
    
        - gt : ����   ���磺ta = Teacher.objects.filter(age__gt=18) # �����������18���
        - gte �����ڵ���
        - lt : С��
        - lte: С�ڵ���
        - range: ��Χ
        - year: ���
        - isnull: �Ƿ�Ϊ��
     2. ���ҵ���ָ��ֵ�ø�ʽ�������� = ֵ  age =18
     3. ģ�����ң� ������_ _(ʹ�����������) = ֵ
     
     * exact �� ��ȷ����
     * iexact�� �����ִ�Сд
     * contains: ����     ta = Teacher.objects.filter(course__contains="")
     * startwith: ��...��ͷ
     * endwith: ��...��β
     
# ģ��-���ݿ���ϵ   
- ������飺���ö�������ϲ���ĳһ����Ϣ�������Ϣ��    
- school:manager 1:1 OneToOne
    - ������ϵ����ģ������һ�߼���
    - add: 
       - ���û�й�ϵ��һ�ߣ�ֱ��ʵ��������Ϳ���                    
            >>>s = School()
            >>> s.school_id=1
            >>> s.school_name="tulingxueyuan"
            >>> s.save()
            >>> ss = School.objects.all()
            >>> ss
            <QuerySet [<School: nanjingtulingxueyuan>, <School: tulingxueyuan>]>
       - ����й�ϵ��һ��,ʹ��ʹ��ʵ��������ʹ��create����,**����ʹ��create**
            1. ʹ��ʵ����������
                >>> m = Manager()
                >>> m.manager_id = 10
                >>> m.manager_name = "dana"
                >>> m.my_school = s
                >>> m.save()
                >>> mm = Manager.objects.all()
                >>> mm
                <QuerySet [<Manager: dana>]>
            2. ʹ��create������
                >>>m = Manager.objects.create(manager_id = 20, manager_name = "erna", my_school=ss[0])
        - Query(��ѯ):
            - ���ӱ��ĸ��  ��ѯdanaУ�����ĸ�ѧУ��
                >>>Manager.objects.get(manager_name="dana").my_school.school_name
            - ��ĸ����ӱ�  ��ѯ�д��õ�ѧУ
                >>>School.objects.get(manager__manager_name="dana")
        - change(�޸�)
            - �����޸���save()
            - �����޸�ʹ��update()
                >>> ss = School.objects.all()
                >>> ss.update(school_name="ͼ��ѧԺ")
            - ���۶��ӱ���ĸ����޸�
        - delete(ɾ��)��ֱ��ʹ��deleteɾ��

- school:teacher 1:N OneToMany
    - ������ϵ��
        - һ������һ�����������ȣ������кܶ����һ������������
        - ���磺һ��ѧУ�����кܶ����ʦ����һ����ʦֻ��һ��ѧУ
        - �ڶ��һ��ʹ��ForeignKey
    - Add(���)
        - ��һ��һ�ķ������ƣ�ͨ��create��new�����
            1. ʹ��ʵ��,��Ҫ�ֶ�save
                >>> ss = School.objects.all()
                >>> ss
                <QuerySet [<School: nanjingtulingxueyuan>, <School: tulingxueyuan>]>
                >>> ss[0]
                <School: nanjingtulingxueyuan>
                >>> t1 = Teacher()
                >>> t1
                <Teacher: >
                >>> t1.teacher_name = "����"
                >>> t1.my_school = ss[0]s
                >>> t1.save()
                >>> ts = Teacher.objects.all()
                >>> ts
                <QuerySet [<Teacher: ����>]>
            2. ʹ��create�������Ƽ���
                >>>t = Teacher.objects.create(teacher_name= "����", my_school = ss[1])
                >>> t
                <Teacher: ����>
                >>> ts
                <QuerySet [<Teacher: ����>, <Teacher: ����>]>
        - create: �����Զ�������Ȼ����Ҫ�ֶ�����
        - new: �������Ի����Ϊ�գ�����save����
    - Query(����)��
        - ��ѧУ����ʦ������Ϊ׼
        - ���֪����ʦ��ѧУ�� ��ͨ�����ӵĹ�ϵ���ԣ�ֱ��ʹ��
        - ���磺����t1��ʦ���ĸ�ѧУ�� 
            >>>t1.my_schools
        - ���飺��ѯѧУ��������ʦ������Ҫ����ʦģ�����Ƶ�Сд��ֱ�Ӽ��»���set��teacher_set
            """һ�Զ�Ĺ�ϵϵͳĬ�����һ�����һ�ߵ�����"""  # teacher_set
            >>>s1.teacher_set.all()
- teacher:student N:N  ManyToMany
    - ��ʾ����һ��������ݿ���ӵ�жԷ����������ݣ���֮��Ȼ
    - ����������ӣ���ʦ��ѧ���Ĺ�ϵ
    - ʹ���ϣ�������һ����ʹ��ManyToMany���壬ֻ��Ҫ����һ��
    -Add(���):
        - �����ʦ����ʹ��student.teachers.add()
        >>>tt = Teacher.objects.all()
        <QuerySet [<Teacher: ����>, <Teacher: ����>]>
        >>>stu = Student()
        >>>stu.teachers.add(tt[0])
        >>>stu.teachers.all()
        <QuerySet [<Teacher: ����>]>
        >>>stu.teachers.add(tt[1])
        >>>stu.teachers.all()
        <QuerySet [<Teacher: ����>, <Teacher: ����>]>
                
    - Query(��ѯ)
        - ��һ�Զ�һ����ʹ��_set
        - ����ѧ����Ӧ��������ʦ ss[0].teachers.all()
        - ������ʦ��Ӧ������ѧ�� tt[0].student_set.all()
        >>> tt = Teacher.objects.all()
        >>> tt
        <QuerySet [<Teacher: ����>, <Teacher: ����>]>
        >>> ss = Student.objects.all()
        >>> ss
        <QuerySet [<Student: ѧ��1>]>
        >>> tt[0].student_set
        <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object
         at 0x0000000003D56860>
        >>> tt[0].student_set.all()
        <QuerySet [<Student: ѧ��1>]>
        >>> ss[0].teachers
        <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object
         at 0x0000000003D56860>
        >>> ss[0].teachers.all()
        <QuerySet [<Teacher: ����>, <Teacher: ����>]>
        
# ģ�� Template(html/css...)
- ģ�壺һ����ͬ�������Ƶ�ҳ�棬����Ҫ���Ի��ĵط��������ף���Ҫ��ʱ��ֻ��Ҫ���������Ϳ�����
- ���裺
    1. ��settings�н������ã�
        - TEMPLATES
    2. ��templates�ļ����±�дģ�岢����
    

# ģ��-����
- �����ı�ʾ������{{var_name}}  
- ϵͳ����ģ���ʱ�򣬻�����Ӧ�����ݲ�����Ӧ�ı������ƣ�������ҵ��������߽���Ⱦ���Ҳ�����������
    # C = dict()
    # C["name"] = "sunlimin"
    >>>render(request, 'two.html', context={"name":"sunlimin"})
- ����two.html

# ģ��-��ǩ
- for��ǩ��{%for .. in ..%}  {% endfor %}
   
    {%for s in score %}
        {{s}}
    {% endfor %}
# if��ǩ
- �����ж�����
- ����ʾ����
    {%if ���� %}
        ��������ִ�����
    {% elif ���� %}
        ��������ִ�����
    {% else %}
        ��������������ִ�����
    {% endif %}
    
    {% if name == "������" %}
        {{name}},���
    {% elif name == "������" %}
        {{name}},hello
    {% endif %}
# csrf��ǩ
- csrf:��վ����α��
- ���ύ����ʱ�򣬱�ҳ����Ҫ����{% csrf_token%},
- ���� five_get,five_post
   
   

        
        