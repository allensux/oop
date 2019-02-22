# coding:utf8

"""
功能名称：
作者：
创建时间：
"""

from selenium.webdriver.common.by import By
from time import sleep
import sys

sys.path.append("../pages/")
from pages.homePage import *

class LoginPage(HomePage):
    #元素定位器，定位页面的元素
    #用户名
    username_loc = (By.ID,"mobilePhone")
    #密码
    passwd_loc = (By.ID,"password")
    #登陆按钮
    loginBtn_loc = (By.CSS_SELECTOR,"a.btn.btn-block.fs-16")
    #退出链接
    logoutBtn_loc = (By.CSS_SELECTOR,"a.fc-blue.mr-5")
    #用户名为空的提示信息
    userNull_loc = (By.CSS_SELECTOR,"#error > span")
    #密码为空的提示信息
    passWordNull_loc = (By.CSS_SELECTOR,"#error > span")

    #打开登陆页面
    def openLoginPage(self):
        self.dr.get(self.url)
        sleep(0.5)
        self.dr.refresh()
        self.dr.maximize_window()
        sleep(0.05)
    #操作元素
    #输入用户名
    def input_userName(self,userName):
        self.find_element(*self.username_loc).send_keys(userName)
    #输入密码
    def input_passWord(self,passWord):
        self.find_element(*self.passwd_loc).send_keys(passWord)
    #点击登陆按钮
    def click_loginBtn(self):
        self.find_element(*self.loginBtn_loc).click()
    #获取登陆成功后的提示信息
    def get_assertText(self):
        return self.find_element(*self.logoutBtn_loc).text
    #用户名为空的提示信息
    def get_userNullText(self):
        return self.find_element(*self.userNull_loc).text
    #密码为空的提示信息
    def get_passWordNullText(self):
        return self.find_element(*self.passWordNull_loc).text