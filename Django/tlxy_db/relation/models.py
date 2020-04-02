# coding:utf8

from django.db import models

# Create your models here.
"""创建模型，一个类对应一个数据库表"""

"""学校类对应学校表"""
class School(models.Model):

    school_id = models.IntegerField()
    school_name = models.CharField(max_length=20)

    """一对多的关系系统默认添加一个属性"""
    # teacher_set

    # my_manager = models.OneToOneField("Manager", on_delete=None)  # 建立OneToOne关系

    def __str__(self):
        return self.school_name

"""校长类对应校长表"""
class Manager(models.Model):
    manager_id = models.IntegerField()
    manager_name = models.CharField(max_length=20)

    # django 升级到2.0之后,表与表之间关联的时候,必须要写on_delete参数,否则会报异常
    my_school = models.OneToOneField(School, on_delete=None)  # 建立OneToOne关系

    def __str__(self):
        return self.manager_name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    my_school = models.ForeignKey(School, on_delete=None)  # 定义一对多的关系，一个学校，对应多个老师

    def __str__(self):
        return self.teacher_name


class Student(models.Model):
    student_name = models.CharField(max_length=20)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.student_name