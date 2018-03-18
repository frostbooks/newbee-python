print('hanoi')
def hanoi(n,x,y,z):
    if n == 1:
        print(x,'->',z)
    else:
        hanoi(n-1,x,z,y)#将n-1个圆盘从x放置到y上面
        print(x,'->',z)
        hanoi(n-1,y,x,z)

n = int(input('please enter an integer:'))
hanoi(n,'X','Y','Z')
