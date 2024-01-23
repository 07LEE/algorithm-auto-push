import sys
import heapq

n = int(sys.stdin.readline())
ans = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        try:
            print(heapq.heappop(ans))
        except IndexError:
            print(0)
    else:
        heapq.heappush(ans, x)