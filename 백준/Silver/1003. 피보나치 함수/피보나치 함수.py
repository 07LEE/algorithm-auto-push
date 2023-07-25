for _ in range(int(input())):
    a = [1, 0]
    b = [0, 1]
    n = int(input())
    
    if n == 0:
        print('1 0')
    elif n == 1:
        print('0 1')
    else :
        for i in range(2, n+1):
            a.append(a[i-1]+a[i-2])
            b.append(b[i-1]+b[i-2])
        print(f'{a[-1]} {b[-1]}')