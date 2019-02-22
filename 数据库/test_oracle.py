# Coding:utf8

import cx_Oracle

host = "10.10.171.249"   #数据库ip
port = "1521"        #端口
sid = "ORCL"         #数据库名称
dsn = cx_Oracle.makedsn(host, port, sid)
conn = cx_Oracle.connect('bbartm','bbartm', dsn) # 连接数据库
c = conn.cursor() #获取cursor
sql = """select * from RTM_BATTERY_PACK where PACK_CODE = 'BBAPELMLLLLLLL88F0000021'"""
x = c.execute(sql) #使用cursor进行各种操作
res = x.fetchall() # 查找全部  feachone()查找一个
print(res)
print(len(res))


# for i in res:
#     print(i)

for i in range(len(res)):
#     print(i)
    print(res[i], end = '')
    for j in range(len(res[i])):
        print(res[i][j])
#for f in range(len(res)):

# enumerate迭代器
# for i,j in enumerate(res):
#     print(i,j)


c.close()     #关闭cursor
conn.close()  #关闭连接
