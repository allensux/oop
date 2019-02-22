#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
import os,time
import pytesseract
import subprocess
import traceback
import logging
import sys
from PIL import Image  # 来源于Pillow库

TESSERACT = r'D:\tools\Tesseract-OCR\tesseract'  # 调用的本地命令名称
TEMP_IMAGE_NAME = "temp.bmp"  # 转换后的临时文件
TEMP_RESULT_NAME = "temp"  # 保存识别文字临时文件
CLEANUP_TEMP_FLAG = True  # 清理临时文件的标识
INCOMPATIBLE = True  # 兼容性标识
# chromedriver =r"C:\Users\USER\AppData\Local\Programs\Python\Python37\chromedriver.exe"
# option = webdriver.ChromeOptions()
# option.binary_location = r'C:\Users\USER\AppData\Local\Google\Chrome\Application\chrome.exe'
# p=r'C:\Users\USER\AppData\Local\Google\Chrome\Application'
# option.add_argument('--user-data-dir='+p)
#browser = webdriver.Chrome()
browser = webdriver.Firefox(executable_path="geckodriver")
# browser = webdriver.Chrome(r"D:\tools\chromedriver.exe")
# print(str(webdriver.ChromeOptions.binary_location))
# browser = webdriver.Chrome(chromedriver,chrome_options=option)
# print(str(webdriver.ChromeOptions.binary_location))

browser.get('http://kq.neusoft.com/')
browser.refresh() #刷新页面
#browser.maximize_window() #浏览器最大化
#获取全屏图片，并截取验证码图片的位置
browser.get_screenshot_as_file('a.jpg')
location = browser.find_element_by_id('imgRandom').location
size = browser.find_element_by_id('imgRandom').size
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']
a = Image.open("a.jpg")
im = a.crop((left,top,right,bottom))
im = im.convert('L')
im.save('a.jpg')
time.sleep(1)
#打开保存的验证码图片
image = Image.open("a.jpg")
#图片转换成字符
vcode = pytesseract.image_to_string(image)
print(str(vcode))

browser.find_elements_by_class_name('textfield')[0].send_keys('liu.mg')
browser.find_elements_by_class_name('textfield')[1].send_keys('wo11223033!')
browser.find_element_by_class_name('a').send_keys(vcode)
browser.find_element_by_id('loginButton').click()
# input_first = browser.find_element(By.ID, 'q')#第一个参数传入名称，第二个传入具体的参数
# print(input_first)
time.sleep(3)
# print(browser.page_source)#browser.page_source是获取网页的全部html
# browser.close()