T = int(input())
for _ in range(T):
    a = 0
    b = 0
    for _ in range(9):
        A, B = map(int, input().split(' '))
        a += A
        b += B
    if a > b :
        print('Yonsei')
    elif b > a :
        print('Korea')
    else :
        print('Draw')