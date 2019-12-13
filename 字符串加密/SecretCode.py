# coding:utf8

"""
功能名称：字符串加密/解密
作者：Allen
创建时间：
"""

# 输入要加密的字符串（大写字母 65-90）
orig_message = "I Love You"

secret_message = ''
# orig_message = orig_message.upper()
# 循环处理字符串中每一个字母
for char in orig_message:
    # print(str(ord(char)))
# 使用ord把字符的Unicode编码取出来
    if char.isalpha():
        secret_message += str((ord(char))-23)
    elif char.isspace():
        secret_message += str(ord(char))

# 打印密文  "2317872318"
print("密文", secret_message)

# 循环把密文字符串两位两位读取进行解密
norm_string = ''
for i in range(0, len(secret_message), 2):
    char_code = secret_message[i] +secret_message[i+1]
    # print(char_code)
    # 读取之后转换编码为字母并组合成字符串
    if char_code != '32':
        norm_string += chr((int(char_code))+23)
    else:
        norm_string += chr(int(char_code))
# 打印string
print(norm_string)