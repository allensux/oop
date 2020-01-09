# coding:utf8

'''
Excel�ļ�תcsv�ļ��ű�
��Ҫ���ýű�ֱ�ӷŵ�Ҫת����Excel�ļ�ͬ��Ŀ¼��
֧��xlsx �� xls ��ʽ
��ͬ��Ŀ¼��������Ϊexcel_to_csv.csv ���ļ�������UTF-8����
'''
import xlrd
import csv
import os
#���ɵ�csv�ļ���
csv_file_name = 'excel_to_csv.csv'
def get_excel_list():
    #��ȡExcel�ļ��б�
    excel_file_list = []
    file_list = os.listdir(os.getcwd())
    for file_name in file_list:
        if file_name.endswith('xlsx') or file_name.endswith('xls'):
            excel_file_list.append(file_name)
    return excel_file_list
def get_excel_header(excel_name_for_header):
    #��ȡ��ͷ��������ͷȫ����ΪСд
    workbook = xlrd.open_workbook(excel_name_for_header)
    table = workbook.sheet_by_index(0)
    #row_value = table.row_values(0)
    row_value = [i.lower() for i in table.row_values(0)]
    return row_value
def read_excel(excel_name):
    #��ȡExcel�ļ�ÿһ�����ݵ�һ���б���
    workbook = xlrd.open_workbook(excel_name)
    table = workbook.sheet_by_index(0) #��ȡ��һ��sheet
    nrows = table.nrows
    ncols = table.ncols
    # ������ͷ���ӵ�һ�����ݿ�ʼ��
    for rows_read in range(1,nrows):
        #ÿ�е����е�Ԫ���������һ���б�
        row_value = []
        for cols_read in range(ncols):
            #��ȡ��Ԫ����������
            ctype = table.cell(rows_read, cols_read).ctype
            #��ȡ��Ԫ������
            nu_str = table.cell(rows_read, cols_read).value
            #�жϷ�������
            # 0 empty,1 string, 2 number(���Ǹ���), 3 date, 4 boolean, 5 error
            #��2������������Ҫ��Ϊint
            if ctype == 2:
                nu_str = int(nu_str)
            row_value.append(nu_str)
        yield row_value

def xlsx_to_csv(csv_file_name,row_value):
    #����csv�ļ�
    with open(csv_file_name, 'a', encoding='utf-8',newline='') as f: #newline=''���ӻ�����
        write = csv.writer(f)
        write.writerow(row_value)
if __name__ == '__main__':
    #��ȡExcel�б�
    excel_list = get_excel_list()
    #��ȡExcel��ͷ������csv�ļ�����
    xlsx_to_csv(csv_file_name,get_excel_header(excel_list[0]))
    #����csv��������
    for excel_name in  excel_list:
        for row_value in read_excel(excel_name):
            xlsx_to_csv(csv_file_name,row_value)
    print('Excel�ļ�תcsv�ļ����� ')