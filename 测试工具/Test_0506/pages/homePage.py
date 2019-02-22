# coding:utf8

"""
功能名称：
作者：
创建时间：
"""

from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#页面基类
class HomePage():
    #初始化页面属性
    def __init__(self,url,driver):
        self.url = url
        self.dr = driver

    #封装元素定位方式
    def find_element(self,*loc):
        ###----- 确保元素是可见的。
        try:
            #以下入参本身是元组，不需要加*
            #WebDriverWait(self.dr,20).until(EC.visibility_of_element_located(loc))
            #以下入参为元组的元素，需要加*
            WebDriverWait(self.dr,20).until(lambda dr:dr.find_element(*loc).is_displayed())
            return self.dr.find_element(*loc)
        except:
            print(*loc+"元素在页面中未找到！")