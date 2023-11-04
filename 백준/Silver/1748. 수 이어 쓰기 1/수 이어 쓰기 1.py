import sys
input = sys.stdin.readline

n = input().strip()
ans = 0

if len(n) == 1:
    ans = n
else:
    ans = 11
    for i in range(2, 10):
        if len(n) == i:
            ans += i*(int(n) - (10**(i-1)))
            break
        else:
            ans += i*(9*10**(i-1))+1
print(ans)