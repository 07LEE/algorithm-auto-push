a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(3):
    c = a[i] - b[i]
    if c < 0:
        ans -= c
print(ans)