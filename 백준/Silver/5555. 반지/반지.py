w = input()
n = int(input())

ans = 0
for _ in range(n):
    m = input()
    if w in m*2:
        ans += 1
print(ans)