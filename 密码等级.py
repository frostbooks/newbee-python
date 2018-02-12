# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

password = input('please enter your password:')
lenth = len(password)
passlen = 0

char = r'~!@#$%^&*()_=-/,.?<>;:[]{}|\ '
num = '1234567890'
alph = 'abcdefghijklmnopqrstuvwxyz'

#判断密码长度
if lenth <= 8:
    passlen = 1
elif 8 < lenth <16:
    passlen = 2
else:
    passlen = 3

passcount = 0

for each in password:
    if each in char:
        passcount += 1
        break

for each in password:
    if each in num:
        passcount += 1
        break

for each in password:
    if each in alph:
        passcount += 1
        break

while True:
    if (passlen == 1) and (passcount ==1):
        print('your password level is low')
    if (passlen == 2) and (passcount ==2):
        print('your password level is mid')
    if (passlen == 3) and (passcount ==3):
        print('your password level is high')

    break



