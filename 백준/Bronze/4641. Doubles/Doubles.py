while True:
    n = list(map(int, input().split()))
    if n[-1] == -1 :
        break
    else:
        cnt = 0
        for i in range(len(n)-1):
            if n[i] * 2 in n:
                cnt += 1
        print(cnt)