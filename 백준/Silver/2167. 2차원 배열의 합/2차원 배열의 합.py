n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    ans = 0
    for p in range(i-1, x):
        for q in range(j-1, y):
            ans += arr[p][q]
    print(ans)