# coding:utf8

"""
功能名称：
作者：
创建时间：
"""

import datetime
import os
# import mssqlhelper
#
# ms = mssqlhelper.MSSQL(host="192.168.0.108", user="sa", pwd="sa", db="ComPrject")

#
# def getAreas(cityid):
#     arealist = ms.ExecQuery("select *From  dbo.areas  where  cityid='%s' " % cityid)
#     return arealist
#
#
# def getCity(provinces):
#     citylist = ms.ExecQuery("select *From  dbo.cities where provinceid='%s'" % provinces)
#     return citylist
#
#
# def getProvinces():
#     provlist = ms.ExecQuery("select *From  dbo.provinces")
#     return provlist


def createFileJson():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    path = date + '-cop.json'
    return path


def writeJson(path,vin):
    # provlist = getProvinces()

    listname = ['A.1']
    with open(path, "w", encoding="utf-8") as f:
        f.write("{\n")
        f.write('\t"A.1": {\n')
        f.write('\t\t"VIN": "%s" \n' %vin)
        f.write("\t}\n")
        f.write("}\n")

if __name__ == '__main__':
    path = createFileJson()
    writeJson(path,'LBVKY91HHHHH000001')


















        # lp = 0
        # for p in provlist:
        #     if lp > 0:
        #         f.write(",\n")
        #     else:
        #         f.write("\n")
        #     f.write("{\n")
        #     f.write('"Code":"%s"\n' % p[1])
        #     f.write(',"Name":"%s"\n' % p[2])
        # f.write(',Nodes:[\n')
            # citylist = getCity(p[1])
            # lc = 0
            # for c in citylist:
            #     if lc > 0:
            #         f.write("\t,\n")
            #     else:
            #         f.write("\n")
            #     f.write("\t{\n")
            #     f.write('\t"Code":"%s"\n' % c[1])
            #     f.write('\t,"Name":"%s"\n' % c[2])
            #     f.write('\t,Nodes:[\n')
            #     # arealist = getAreas(c[1])
            #     la = 0
            #     for a in arealist:
            #         if la > 0:
            #             f.write("\t\t,\n")
            #         else:
            #             f.write("\n")
            #         f.write("\t\t{\n")
            #         f.write('\t\t"Code":"%s"\n' % a[1])
            #         f.write('\t\t,"Name":"%s"\n' % a[2])
            #         f.write("\t\t}\n")
            #         la += 1
            #     f.write("\t]\n")
            #     f.write("\t}\n")
            #     lc += 1
            # f.write("]\n")
            # f.write("}\n")
            # lp += 1


