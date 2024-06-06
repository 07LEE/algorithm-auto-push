N = int(input())
W = input()
check = 0

if N == 2 and W[0] == W[1]:
    print('NO')
else:
    for i in range(1, N):
        cnt = 0
        a = list(W[:i])
        b = list(W[-i:])
        for j in range(i):
            if a[j] != b[j]:
                cnt += 1
        if cnt == 1:
            check += 1
    print('YES') if check != 0 else print('NO')