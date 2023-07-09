n, k = map(int, input().split())
num = [False] * (n+1)
cnt = 0
for i in range(2, n+1):
    if num[i] == False:
        for j in range(i, n+1, i):
            if num[j] == False:
                num[j] = True
                cnt += 1
                if cnt == k:
                    print(j)
