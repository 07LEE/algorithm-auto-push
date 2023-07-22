n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0
cost = b[0]

for i in range(n-1):
    if cost > b[i]:
        cost = b[i]
    res += cost * a[i]

print(res)