# coding:utf8

"""
功能名称：IPM报文--电池包
作者：
创建时间：
"""
from Tools.scripts.treesync import raw_input

"""当前目录创建txt文件"""
def createFileTxt():
    path = 'ipm.txt'
    return path


"""生成电池包报文"""
def write_ipm_pack(path, count):
    ipm_title = 'IPRT_W89IPM__W89RTM     19730911-10:00:00109HVBSNRHVB401'
    ipm_mmo_title = 'MMO         '
    ipm_chv_title = 'CHV         '
    ipm_mod_title = 'MODSNRMOD401'
    ipm_cel_title = 'CELSNRCEL401'
    ipm_cmo_title = 'CMO         '
    ipm_cce_title = 'CCE         '
    bind = '1'  # 绑定
    unbind = '0'  # 解绑

    with open(path, "w", encoding="utf-8") as f:
        pack_hvb_list = []
        for i in range(1, count+1):
            m = str(i).zfill(5)  # 字符串，补齐5位，不够前面补0
            hvb_code = 'BMWIPM000PACK0000000BMW000' + m
            mmo_list = []
            chv_list =[]
            pack_hvb_list.append(hvb_code)
            # print('电池包hvb',pack_hvb_list)
            f.write(ipm_title + pack_hvb_list[i-1])  # 写入title与hvb信息

            """循环MMO与CHV"""
            for j in range((i-1)*4+1,i*4+1):
                n =str(j).zfill(5)
                if(j == (i-1)*4 +1):
                    mmo_code = '005' + ipm_mmo_title +'DOUBLEBBMW00BMW' + n +'           '

                    chv_code = bind + ipm_chv_title + '001PAIPMIPMIPM66F00' + m + '       '
                else:
                    mmo_code = bind + ipm_mmo_title +'DOUBLEBBMW00BMW' + n +'           '
                # mod_code = '002' + ipm_mod_title + 'BMWIPM000MODULE00000BMW000' + n
                mmo_list.append(mmo_code)
                chv_list.append(chv_code)

                print('双模块:', mmo_list)
                print('电池包chv',chv_code)
                f.write(mmo_list[j-((i-1)*4+1)])  # 写入双模块MMO信息
            f.write(chv_list[j-((i-1)*4+1)])   # 写入chv信息


            """循环MMO与MOD"""
            mmo_list_1 = []
            mod_list= []

            for k in range((i-1)*4+1,i*4+1):
                o = str(k).zfill(5)
                # if(k ==(i-1)*4 +1):
                mmo_code_1 = bind + ipm_mmo_title + 'DOUBLEBBMW00BMW' + o + '           '
                mmo_list_1.append(mmo_code_1)
                print('双', mmo_list_1)
                f.write(mmo_list_1[k-((i-1)*4+1)])  # 写入双模块MMO信息

                for k1 in range((k-1)*2+1,k*2+1):
                    if(k1 % 2 ==1):
                        mod_code = '002' + ipm_mod_title + 'BMWIPM000MODULE00000BMW000' + str(k1).zfill(5)
                    else:
                        mod_code = bind + ipm_mod_title + 'BMWIPM000MODULE00000BMW000' + str(k1).zfill(5)
                    mod_list.append(mod_code)
                    print('模块', mod_list)
                    f.write(mod_list[k1-((i-1)*8+1)])  # 写入单模块MOD信息


            """循环MOD与CEL、CMO"""
            mod_list_1 = []
            cel_list = []
            cmo_list = []
            for m in range((i-1)*8+1,i*8+1):
                mod_code_1 = bind + ipm_mod_title + 'BMWIPM000MODULE00000BMW000' + str(m).zfill(5)
                cmo_code = bind + ipm_cmo_title + '001MAIPMIPMIPM66F00' + str(m).zfill(5) + '       '
                cmo_list.append(cmo_code)
                mod_list_1.append(mod_code_1)
                print('单模块：',mod_list_1)
                f.write(mod_list_1[m-((i-1)*8+1)])  # 写入单模块MOD信息

                for m1 in range((m-1)*12+1,m*12+1):
                    if(m1 %12==1):
                        cel_code = '013' + ipm_cel_title + 'BMWIPM000CELL0000000BMW000' + str(m1).zfill(5)
                    else:
                        cel_code = bind + ipm_cel_title + 'BMWIPM000CELL0000000BMW000' + str(m1).zfill(5)
                    cel_list.append(cel_code)
                    print('单体', cel_list)
                    f.write(cel_list[m1-((i-1)*96+1)])  # 写入单体CEL信息
                f.write(cmo_list[m-((i-1)*8+1)]) # 写入单模块CMO信息


            """循环CEL与CCE"""
            cel_list_1 = []
            cce_list = []
            for n in range((i-1)*96+1,i*96+1):
                cel_code_1 = bind + ipm_cel_title + 'BMWIPM000CELL0000000BMW000' + str(n).zfill(5)
                cce_code = '001' + ipm_cce_title + '001CAIPMIPMIPM66F00'  + str(n).zfill(5) + '       '
                cel_list_1.append(cel_code_1)
                cce_list.append(cce_code)
                print('单体BMW',cel_list_1)
                print('单体GBT',cce_list)
                f.write(cel_list_1[n - ((i - 1) * 96 + 1)])  # 写入单体CEL信息
                f.write(cce_list[n - ((i - 1) * 96 + 1)])  # 写入单体CCE信息

            f.write('1\n') # 换行


if __name__ == '__main__':
    path = createFileTxt()
    write_ipm_pack(path,int(raw_input("请输入一个大于0的整数: (输入1，生成1条报文; 输入2，生成2条报文)\n")))