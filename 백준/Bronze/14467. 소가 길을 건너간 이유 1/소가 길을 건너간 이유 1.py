n = int(input())
caw = [-1] * 11
ans = 0

for _ in range(n):
    a, b = map(int, input().split())
    if caw[a] == -1:
        caw[a] = b
    else:
        if caw[a] != b:
            ans += 1
            caw[a] = b

print(ans)