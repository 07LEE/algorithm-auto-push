a = int(input())
b = int(input())
if a >= b :
    print('Congratulations, you are within the speed limit!')
elif b-a >= 31:
    print('You are speeding and your fine is $500.')
elif b-a >= 21:
    print('You are speeding and your fine is $270.')
else:
    print('You are speeding and your fine is $100.')