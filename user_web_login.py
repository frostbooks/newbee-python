print('----welcome to our website----')
print('1.sign up')
print('2.login')
print('3.delete account')
accounts = {'eddy':'338126'}
import random
active = True
while active:
    chances = 3
    quest = int(input('Please enter your quest number: ',))
    if quest == 1:
        active_1 = True
        while active_1:
            name = input('Please enter your name: ')
            if name not in accounts.keys():
                print('this name is free to use')
                active_1 = False
            else:
                print('sorry,this name has been used.')
                continue
            password = input('please enter your password:')
            accounts[name] = password
            print('your account has been signed up,login in now!')
    if quest == 2:
        active_2 = True
        while active_2:
            name = input('Please enter your name: ')
            if name not in accounts.keys():
                print('this account does not exist,sign it up first.')
                break
            else:
                while chances:
                    password = input('please enter your password:')
                    if password == accounts[name]:
                        print('correct,welcome!')
                        active = False
                        break
                    else:
                        chances -= 1
                        if chances == 0:
                            print('sorry,your account has been locked.')
                            break
                        print('sorry,your password is not correct,you have ' + str(chances) + ' time left.')
                break
    if quest == 3:
        active_3 = True
        while active_3:
            name = input('Please enter your name: ')
            if name not in accounts.keys():
                print('this account does not exist,sign it up first.')
                break
            else:
                while chances:
                    password = input('please enter your password:')
                    if password == accounts[name]:
                        yes_no = input('are you sure to delete your account(enter yes or no):')
                        if yes_no == 'yes':
                            del accounts[name]
                            break
                        else:
                            break
                    else:
                        chances -= 1
                        if chances == 0:
                            print('sorry,your account has been locked.')
                            break
                        print('sorry,your password is not correct,you have ' + str(chances) + ' time left.')
                break











