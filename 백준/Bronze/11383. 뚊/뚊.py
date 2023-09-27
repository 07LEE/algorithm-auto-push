n = list(map(int, input().split()))
a, b = [], []

for _ in range(n[0]):
    a.append(list(input()))
for _ in range(n[0]):
    b.append(list(input()))

ans = 'Eyfa'

for i in range(n[0]):
    for j in range(1, n[1]+1):
        if a[i][j-1] != b[i][j*2-1] or a[i][j-1] != b[i][j*2-2] :
            ans = 'Not Eyfa'

print(ans)