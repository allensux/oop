# coding:utf8

from selenium import webdriver
from PIL import Image, ImageEnhance
import pytesseract
import pytesser3
from time import sleep
# from selenium.webdriver.common.keys import Keys


def clock():
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox(executable_path="geckodriver")
    driver.get("http://kq.neusoft.com/")
    driver.implicitly_wait(3)
   # driver.maximize_window()
    sleep(1)
    driver.find_element_by_xpath("//*[@id='tbLogonPanel']/div/div/div[2]/div[2]/input").send_keys("sun-lm")
    sleep(1)
    driver.find_element_by_xpath("//*[@id='tbLogonPanel']/div/div/div[2]/div[3]/input").send_keys("$RFV4rfv4")

    """
    图片截取与验证码识别
    """
   #  text = pytesseract.image_to_string(i4, lang='chi_sim')
   #  print(text)

    # pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)//Tesseract-OCR//tesseract.exe'
    # tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    # tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'

    driver.save_screenshot(r"E:\aa.png")
    img = driver.find_element_by_id("imgRandom")  # 定位验证码
    location = img.location  # 获取验证码x,y轴坐标
    size = img.size  # 获取验证码的长宽
    coderange = (
    int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
    # 写成我们需要截取的位置坐标
    i = Image.open(r"E:\aa.png")  # 打开截图
    frame4 = i.crop(coderange)  # 使用Image的crop函数，从截图中再次截取我们需要的区域

    # 打开保存的验证码图片
    #image = Image.open("a.jpg")
    #
    # frame4.save(r"E:\frame4.png")
    # i2 = Image.open(r"E:\frame4.png")
    imgry = frame4.convert('L')  # 图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
    #sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
    #i3 = sharpness.enhance(3.0)  # 3.0为图像的饱和度
    imgry.save("E:\\image_code.png")
    img = Image.open("E:\\image_code.png")
    text = pytesseract.image_to_string(img)  # 使用image_to_string识别验证码
    print(text)
    sleep(1)
    driver.find_element_by_xpath("//*[@id='tbLogonPanel']/div/div/div[2]/div[4]/input").send_keys(text)
    sleep(1)
    #driver.find_element_by_id("loginButton").click()
    driver.quit()

if __name__ == '__main__':
    clock()





