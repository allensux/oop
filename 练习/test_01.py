# coding:utf8

"""
功能名称：
作者：
创建时间：
"""
#
# str = " random access man"
#
# str = str.upper()
#
# lisOfWords = str.split()
# print(lisOfWords)
# for word in lisOfWords:
#     print(word[0], end='')
#
#


import random

def add(times):
    while times>0:
        add_param1=random.randint(1,100)
        add_param2=random.randint(1,100)
        correct_result = add_param1 + add_param2
        input_result=input("{}+{}=".format(add_param1, add_param2))
        if str(correct_result) == input_result:
            print("回答正确！你真棒！")
        else:
            print("还需要更细心噢！正确答案是" + str(correct_result))
        times -= 1

def mul(times):
    while times>0:
        mul_param1=random.randint(1,100)
        mul_param2=random.randint(1,10)
        correct_result = mul_param1 * mul_param2
        input_result=input("{}*{}=".format(mul_param1, mul_param2))
        if str(correct_result) == input_result:
            print("回答正确！你真棒！")
        else:
            print("还需要更细心噢！正确答案是" + str(correct_result))
        times -= 1

def main():
    while True:
        cmd=input("请输入指令（a/m/q）：")
        if cmd=='q':
            print("小明再见！你会回来的")
            break
        elif cmd=='a':
            add(5)
        elif cmd=='m':
            mul(3)
        else:
            print("指令错误，请重新输入！")

if __name__ == '__main__':
    main()
