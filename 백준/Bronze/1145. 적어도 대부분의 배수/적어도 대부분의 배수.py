num = list(map(int, input().split()))
n = min(num)
while True:
    cnt = 0
    for i in range(len(num)):
        if n%num[i] == 0:
            cnt += 1
    if cnt >= 3:
        print(n)
        break
    n += 1