import sys
import collections
input = sys.stdin.readline

N = collections.deque([i for i in range(1, int(input())+1)])
while len(N) != 1:
    N.popleft()
    N.rotate(-1)
print(N[0])