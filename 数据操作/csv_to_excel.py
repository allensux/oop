# coding:utf8

"""
功能名称：将csv转换成多个excel pd格式
作者：Allen
创建时间：2020/01/09
"""
import os
import pandas as pd


def get_csv_list():
    # 获取csv文件列表
    csv_file_list = []
    file_list = os.listdir(os.getcwd())
    for file_name in file_list:
        if file_name.endswith('csv'):
            csv_file_list.append(file_name)
    return csv_file_list


def csv_to_xlsx_pd():
    csv_list = get_csv_list()
    # print(len(csv_list))
    for i in range(len(csv_list)):
        csv = pd.read_csv(csv_list[i], encoding='GBK')  # 使用国标码编码gb2312、GBK也OK
        csv.to_excel('csv_to_excel_' + str(i) + '.xlsx' , sheet_name='data')  # 生成N个excel文件


if __name__ == '__main__':
    csv_to_xlsx_pd()