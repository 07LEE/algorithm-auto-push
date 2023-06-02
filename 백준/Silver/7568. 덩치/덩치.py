n = int(input())

ans = [1] * n
data = []

for _ in range(n):
    a = list(map(int, input().split()))
    data.append(a)

for i in range(n):
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            ans[i] += 1

print(*ans)