import sys
input = sys.stdin.readline

ans = 0
n = [int(input()) for _ in range(10)]

for i in n:
    ans += i
    if ans >= 100:
        if ans - 100 > 100 - ans + i:
            ans -= i
        break

print(ans)