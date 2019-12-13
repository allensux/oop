# coding:utf8

"""
功能名称：
作者：
创建时间：
"""
"""不定数量参数累加"""
# def get_sum(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
# print("Sum = ", get_sum(3,5,4))

def isprime(num):
    for i in range(2, num):
        if (num%i) == 0:
            return False
    return True

def getPrime(maxNum):
    list1 = []
    for i in range(2, maxNum):
        if isprime(i):
            list1.append(i)
    return list1

input_num = int(input("查找所有素数："))

listOfPrimes = getPrime(input_num)
print(listOfPrimes)
# for prime in listOfPrimes:
#     print(prime)


