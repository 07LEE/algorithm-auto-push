import sys
input = sys.stdin.readline

N = int(input())
stops = [int(input()) for i in range(N)]
ans = 0
for i in range(N-1):
    ans += (stops[i+1] - stops[i])**2
print(ans)