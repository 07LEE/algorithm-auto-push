n = int(input())
num = list(map(int, input().split()))
ans = []

for i, j in enumerate(num):
    if len(ans) == 0:
        ans.append(i+1)
    else:
        ans.insert(len(ans)-j, i+1)

print(*ans)