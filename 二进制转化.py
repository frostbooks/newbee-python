def trans(num):
    temp = str(num)
    if not temp.isdigit():
        print('please enter a number!')
    else:
        list1 = []
        result = ' '
        while num :
            a = num % 2
            num = num //2
            list1.append(a)
        while list1:
            result += str(list1.pop())
        print(result)
                      
