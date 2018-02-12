times = 3
password =123456
while times:
    temp = input('please enter your password:')
    if ('*' in temp):
        print('sorry,password cannot include "*"')
    elif not temp.isdigit():
        times -= 1
        print('sorry ,your password is wrong.')
        continue
    else:
        enter = int(temp)
        if enter == password:
            print('right')
            break
        else:
            times -= 1
            print('wrong')
        
        
   

    
