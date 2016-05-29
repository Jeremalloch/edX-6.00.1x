print('Please think of a secret number between 0 and 100')
x=25
c=145
low=0
high=100
while x != 'c':
    ans=int((high + low)/2)
    print('')
    print('Is your secret number ' + str(ans) + '?'),
    x=str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly:"))
    if x == 'h':
       high = ans
    elif x == 'l':
        low = ans
    elif x =='c':
        break
    else:
        print('Invalid input'),
print('Game over n00b. Your so called secret number was' + str(ans))