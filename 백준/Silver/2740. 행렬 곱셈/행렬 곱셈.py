n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
b = []
for _ in range(m):
    b.append(list(map(int, input().split())))

ans = [[0 for _ in range(k)] for _ in range(n)]

for N in range(n):
    for M in range(m):
        for K in range(k):
            ans[N][K] += a[N][M] * b[M][K]

for i in ans:
    print(*i)