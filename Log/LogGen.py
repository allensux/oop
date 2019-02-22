# coding:utf8
import logging
import os
import time


logger = logging.getLogger("logtest")
logger.setLevel(logging.INFO)

ltime = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

logfilename = os.path.dirname(os.path.abspath('.')) + '\\log1\\' + ltime +'.txt'

fileh = logging.FileHandler(logfilename)
fileh.setLevel(logging.INFO)

consolh = logging.StreamHandler()
consolh.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileh.setFormatter(formatter)
consolh.setFormatter(formatter)

logger.addHandler(fileh)
logger.addHandler(consolh)

logger.info('hello,first info test')

