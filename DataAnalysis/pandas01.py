# coding:utf8

"""
功能名称：
作者：
创建时间：
"""

import pandas as pd
from pandas import DataFrame

df = pd.read_csv('data.csv')
# print(df)
print(df.head(2))
print(type(df))
# print(df.min())

print(df.columns)  # 列名
print(df.values)  # 值
print(df.index)  # 索引
print('**************')
print(df.loc[0])
print('**************')
print((df.数学 >= 90) & (df.语文 >80))
print(type(df.数学))
print('**************')
print(df.sort_values)
print('**************')
print(df.sort_values(['数学','语文']).head())

"""访问"""

print(df.loc[0])

"""索引"""

scores = {
    '英语':[90,70,80],
    '数学':[64,78,45],
    '姓名':['孙','王','李']
}
df = pd.DataFrame(scores)
# df = pd.DataFrame(scores, index= ['one','two','three'])
print(df)
print(df.index)
# print(df.loc['two'])
print(df.iloc[1])  # 索引不是数字索引可以用iloc

# print(df.ix[[0],'数学'])  # 过时了，不支持使用

# head = ["表头1" , "表头2" , "表头3"]
# l = [[1 , 2 , 3],[4, 5, 6] , [8 , 7 , 9]]
# df = pd.DataFrame (l , columns = head)
# print(df)
print(''.center(50,'*'))
print(df.loc[0:1])
"""   英语  数学 姓名
0  90  64  孙
1  70  78  王"""
# print(df[0])  # 不可以
# print(df[0:1])  # 可以切片

"""DataFrame中的数组"""
print('df.数学',df.数学.values)  # [64 78 45]
print('统计：',df.数学.value_counts())  #  统计有多少人得多少分
"""
78    1
45    1
64    1
"""

print(df.head())
"""提取多列"""
print(df[['数学','英语']])

"""分类 map"""
def func(score):
    if score >= 70:
        return '优秀'
    else:
        return '垃圾'
df['数学分类'] = df.数学.map(func)
print(df)

def func1(number):
    return str(number) + '-'
print(df.applymap(func1))

print(df.applymap(lambda x: str(x) + '-'))  # 匿名函数

print(df.apply(lambda x: x.数学 +100, axis=1))  # 对每个元素

# 根据多列生成新列数据
df['new_score'] = df.apply(lambda x: x.数学 + x.英语, axis=1)
print(df)
"""   
  英语  数学 姓名 数学分类  new_score
0  90  64  孙   垃圾        154
1  70  78  王   优秀        148
2  80  45  李   垃圾        125
"""
df.head()  # 前几行
df.tail()  # 后几行

# pandas中的dataframe操作，很大一部分跟numpy中的二维数组是近似的





