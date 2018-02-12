import random
times = 3
guess = 0
secret = random.randint(1,10)
while (guess != secret) and(times > 0):
    temp = input('please enter a number:')
    while not temp.isdigit():
        temp = input('sorry,please enter an integral number:') 
    guess = int(temp)
    if guess == secret:
        print('wow,how could you ??')
    else:
        if guess > secret:
            print('big')
        else:
            print('small')
        times -=1
        if times > 0:
            print('one more time!')
        else:
            print('sorrrrry')
print('end~')
