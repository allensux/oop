# coding:utf8

"""
功能名称：
作者：
创建时间：
"""

from selenium import webdriver
from time import sleep
import unittest, sys

sys.path.append("../operatePages/")
sys.path.append("../pages/")
sys.path.append("./")
from operatePages.operateLoginPage import *
from pages.homePage import *

# 导入xlrd模块
import xlrd

# 1、打开excel
data = xlrd.open_workbook(r"E:\untitled\testCases\参数化数据.xlsx")
# 读取用户名和密码所在的页面的数据
sheet1 = data.sheet_by_index(0)
# 获取用户名
userNames = sheet1.col_values(0)
# 获取密码
passWords = sheet1.col_values(1)
# 获取预期结果
exceptResults = sheet1.col_values(2)


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.gjfax.com/toLogin"
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(20)
        # 实例化一个operateLoginPage类的对象
        self.loginPage = LoginPage(self.url, self.dr)

    # 测试正常登陆
    def testLogin(self):
        # 打开登陆页面
        self.loginPage.openLoginPage()
        # 输入用户名
        self.loginPage.input_userName(userNames[1])
        # 输入密码
        self.loginPage.input_passWord(passWords[1])
        # 点击登陆
        self.loginPage.click_loginBtn()
        # 断言
        self.assertEqual(exceptResults[1], self.loginPage.get_assertText())

    # 测试用户名为空
    def test_user_null(self):
        # 打开登陆页面
        self.loginPage.openLoginPage()
        # 输入用户名
        self.loginPage.input_userName(userNames[2])
        # 输入密码
        self.loginPage.input_passWord(passWords[2])
        # 点击登陆
        self.loginPage.click_loginBtn()
        # 断言
        self.assertEqual(exceptResults[2], self.loginPage.get_userNullText())

    # 测试密码为空
    def test_password_null(self):
        # 打开登陆页面
        self.loginPage.openLoginPage()
        # 输入用户名
        self.loginPage.input_userName(userNames[3])
        # 输入密码
        self.loginPage.input_passWord(passWords[3])
        # 点击登陆
        self.loginPage.click_loginBtn()
        # 断言
        self.assertEqual(exceptResults[3], self.loginPage.get_passWordNullText())

    def tearDown(self):
        self.dr.quit()


if __name__ == "__main__":
    unittest.main()