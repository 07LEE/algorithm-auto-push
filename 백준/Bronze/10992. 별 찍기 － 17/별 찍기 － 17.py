n = int(input())
if n == 1:
    print('*')
else:
    print(' ' * (n-1) + '*')
    for i in range(1, n-1):
        print(' ' * (n - i - 1) + '*' + ' ' * (i * 2 - 1) + '*')
    print('*' * (n * 2 - 1))