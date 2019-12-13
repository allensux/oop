# coding:utf8

"""
功能名称：凯撒加密
作者：Allen
创建时间：
"""
# X Y Z A B C D E F
# A B C D E F G H I

# 接收消息与字母偏移量
message = input("Enter your message： ")
key = input("偏移量（-26~26）")

# 准备密文
secret_message = ''

# 循环一个字符一个字符处理
for char in message:
    # if it is a letter
    if char.isalpha():
        # Get unicode and add the shift
        char_code = ord(char) + str(key)
        # if uppercase
        if char.isupper():
            # if greater than 'Z'
            if char_code > ord('Z'):
                char_code -= 26
            # if less than 'A'
            if char_code < ord('A'):
                char_code += 26
        # if lowercase
        if char.islower():
            # if greater than 'z'
            if char_code > ord('z'):
                char_code -= 26
            # if less than 'a'
            if char_code < ord('a'):
                char_code += 26
        # convert from code to letter and add a message
        secret_message += chr(char_code)
    # if not a letter leave the character as is
    else:
        secret_message += char
# 打印密文
print(secret_message)