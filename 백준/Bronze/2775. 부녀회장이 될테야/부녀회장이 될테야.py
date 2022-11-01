import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    apart = [[i for i in range(1, n+1)]] # 0층
    for i in range(k):
        ment = [1]
        for j in range(1, n):
            ment.append(apart[i][j] + ment[-1])
        apart.append(ment)
    print(apart[-1][-1])