# coding:utf8

"""
文件为censuspopdata.xlsx
用字典数据存储读取出来的数据：
字典中嵌套字典
{'AL':{'Autauga':{'tract':12, 'pop':sum},
        'Baldwin':{},
        .
        .
        .
        'Bibb':{}
'AK': {
        }
        }
}
countryData['AL']['Autauga']['tract']
"""

import openpyxl,pprint

# 打开workbook
print('Opening workbook')
wb = openpyxl.load_workbook('censuspopdata.xlsx')

# 打开表单：
print("Opening worksheet")
# ws = wb.get_sheet_by_name('Population by Census Tract')
sheet = wb.active

countryData = {}

for row in range(2, sheet.max_row+1):
    # 对每一个统计都有一个数据
    state = sheet['B'+ str(row)].value
    country = sheet['C'+ str(row)].value
    pop = sheet['D' + str(row)].value

    # 确定state这个键值存在 字典变量的方法函数setdefault(键，默认值)
    countryData.setdefault(state, {})
    countryData[state].setdefault(country,{'tracts':0, 'pop':0})
    countryData[state][country]['tracts'] += 1
    countryData[state][country]['pop'] += int(pop)

# 打开一个text文本，写入数据
print("Writing results...")
# resultFile = open('census2013.py', 'w')
#
# str = pprint.pformat(countryData)
# resultFile.write('alldata = '+ str)


# with open ('census2014.py', 'w') as f:
#     f.write(str(countryData))

with open ('census2014.txt', 'w') as f:
    f.write('allData =' + pprint.pformat(countryData))