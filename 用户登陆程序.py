print('welcome to the website')
print('---1,login in the site---')
print('---2,sign up an account---')
print('---3,delete an account---')
print('---4,close this page---')
a = {'frost':'eddy338126','frostbooks':'338126'}
import random

while True:
    count = 3
    code = int(input('please enter your quest number:'))
    if code == 1:
        username = input('please enter your username:')
        if username in a:
            while (count > 0):
                password = input('please enter your password:')
                if password != a[username]:
                    print('sorry,your password is not correct!')
                    count -= 1
                    if count == 0:
                        print('you have no chance left')
                        break
                    else:
                        print('you have '+(('%s') % (count))+' time left.')
                else:
                    print('welcome to the website!')
                    break            
        else:
            print('sorry,this username does not exist.')

    if code == 2:
        while True:
            username = input('please enter your username:')
            if username in a:
                print('sorry,this username has been used,try another one.')
                continue
            else:
                password = input('please enter your password:')
                a[username] = password
                while True:
                    rannum = random.randint(1000,9999)
                    print('please enter the verify number '+('%s') % (rannum),end = ' ')
                    temp = int(input())
                    if temp == rannum:
                        print('correct')
                        print('successfully,login in now!!!')
                        break
                    else:
                        print('incorrect')
                    
                break
            
    if code == 3:
        while True:
            username = input('please enter your username:')
            if username not in a:
                print('sorry,your username does not exist,try again.')
                continue
            else:
                while (count > 0):
                    password = input('please enter your password:')
                    if password == a[username]:
                        print('Correct,are you sure to delete this account?please enter Y or N',end = ' ')
                        temp = input()
                        if temp == 'Y':
                            a.pop(username)
                            print('user: '+username+' has been deleted.')
                            break
                        else:
                            break
                    else:
                        print('sorry,your password is not correct!')
                        
                        count -= 1
                        if count == 0:
                            print('you have no chance left')
                            break
                        else:
                            print('you have '+(('%s') % (count))+' time left.')
                break

    if code == 4:
        print('Are you sure to leave this page?(Y or N)',end = ' ')
        temp = input()
        if temp =='Y':
            print('bye')
            break

f = open('E:\\test.txt','w') 
for each in a.items():
    each = str(each)
    f.write(each)

f.close()
            
        
        
            
                
            

    
                    
                    
                
                
    
