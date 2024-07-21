N = int(input())
ans = {}
for _ in range(N):
    _, x = input().split('.')
    if x in ans:
        ans[x] = ans[x] + 1
    else:
        ans[x] = 1

name = sorted(ans)
for i in name:
    print(i, ans[i])