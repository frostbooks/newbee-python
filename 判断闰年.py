print('-----whether a leap year?-----')
temp = input('please enter a year\'s number:')
while not temp.isdigit():
    temp = input('sorry,please enter a integral number:')
number = int(temp)
if number % 4 != 0:
    print('year ' + temp + ' is not a leap year')
elif (number % 100 == 0) and (number %400 != 0 ):
    print('year ' + temp + ' is not a leap year')
else:
    print('year ' + temp + ' is a leap year')
