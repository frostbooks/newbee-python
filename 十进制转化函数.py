def trans(num):
    temp = str(num)
    if not temp.isdigit():
        print('please enter a number')
    else:
        temp16 =str('%x' % num)
        print('十六进制为:' + temp16 )
        temp8 =str('%o' % num)
        print('八进制为:' + temp8 )
