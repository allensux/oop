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
    - conda create -n env_name python=3.6
- ����conda�����⻷��
    - (win)conda activate env_name  
           conda activate slm # 
- ��װdjango��
    - pip install django==2.1.4
    - conda install django==2.1.4���Ƽ���

    
# ��̨��Ҫ������

#### ������һ��django��Ŀ
   django-admin startproject tulingxueyuan
    
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
    - �������python manage.py startapp teacher
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
                