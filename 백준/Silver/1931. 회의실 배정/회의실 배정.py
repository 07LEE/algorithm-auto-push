n = int(input())
time = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
ans = end = 0
for i, j in time:
    if i >= end:
        ans += 1
        end = j
print(ans)