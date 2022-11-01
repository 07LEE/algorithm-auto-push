import sys
input = sys.stdin.readline
ans = 0
T = int(input())
for t in range(1, T+1):
    N = input()
    n = [N[i-1] for i in range(1, len(N)) if N[i-1] != N[i]]
    if len(n) == len(set(n)):
        ans += 1
print(ans)