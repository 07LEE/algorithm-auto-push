n = int(input())
p = list(map(int, input().split()))

ans = []
num = 0
for i in range(1,n):
    if p[i] > p[i-1]:
        num += p[i] - p[i-1]
        if i == n-1:
            ans.append(num)
    else:
        ans.append(num)
        num = 0

print(max(ans))