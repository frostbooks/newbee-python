print('斐波那契数列')
def fab(n):
    if n < 1:
        print('输入有误')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1) +fab(n-2)
    
number = int(input('please enter an integer:'))
Sum = []
for i in range(1,number,1):
    result = fab(i)
    Sum.append(result)
    print('%d天一共有%d只小兔子' % (i,result))
list1=list(zip(range(1,number),Sum))
print(list1)



