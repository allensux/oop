# coding:utf8

"""
功能名称：将csv转换成excel pd格式
作者：
创建时间：
"""
import os
import pandas as pd


# 生成的excel文件名
excel_file_name = 'csv_to_excel.xlsx'


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
    csv = pd.read_csv(csv_list[0], encoding='GBK')  # 使用国标码编码gb2312、GBK也OK
    csv.to_excel(excel_file_name, sheet_name='data')


if __name__ == '__main__':
    csv_to_xlsx_pd()