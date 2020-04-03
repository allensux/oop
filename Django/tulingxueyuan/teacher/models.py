# coding:utf-8
from django.db import models

# Create your models here.

class Teacher(models.Model):

    name = models.CharField(max_length= 12)  # 姓名
    age = models.IntegerField()  #  年龄
    address = models.CharField(max_length=50)  # 地址
    course = models.CharField(max_length=20)  # 课程


    """ dana = Teacher()  # 创建一个类的实例
        dana.nama = "Dana"  # 属性赋值
        dana.age = 18
        dana.address = "tulingxueyuan"
        
        dana.save()  # 将所有保存到数据库中
        
        """
    """魔法函数--当需要显示实例的时候，显示字符串
    >>> from teacher.models import Teacher
    >>> Teacher.objects.all()
        <QuerySet [<Teacher: Dana>]>
    """
    def __str__(self):
        return self.name