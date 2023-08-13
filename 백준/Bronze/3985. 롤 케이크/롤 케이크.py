l = int(input())
n = int(input())
cake = [0] * (l + 1)
peo, num = 0, 0

for i in range(n):
    p, k = map(int, input().split())
    if k-p > num :
        peo = i +1
        num = k-p
    for j in range(p, k+1):
        if cake[j] == 0:
            cake[j] = i + 1
print(peo)
num = 0
for i in range(1, n+1):
    if cake.count(i) > num:
        num = cake.count(i)
        peo = i

print(peo)