# coding:utf8

"""
功能名称：
作者：
创建时间：
"""

import unittest
from HTMLTestRunner import HTMLTestRunner
import time

import sys
#临时改变工作路径
sys.path.append("./operatePages/")
sys.path.append("./pages/")

if __name__ == "__main__":
    #定义测试用例所在的路径
    casesPath = "./testCases/"
    #定义测试报告所在的路径
    reportPath = "./reports/"
    #定义测试报告的名称
    reportName = time.strftime("%Y-%m-%d %H%M%S",time.localtime()) + '.html'
    #定义测试报告所在的路径和名称
    reportPathName = reportPath + reportName
    #把测试用例组装到unittest的discover容器
    discover = unittest.defaultTestLoader.discover(casesPath,"*.py")
    #打开测试报告，并赋予读写权限
    fp = open(reportPathName,"wb")
    #把测试结果写进测试报告，并装载到HTHMLTestRunner模块
    run = HTMLTestRunner(stream=fp,title="ecshop自动化测试报告",description="用例执行情况")
    #运行脚本
    run.run(discover)
    #关闭打开的测试报告
    fp.close()