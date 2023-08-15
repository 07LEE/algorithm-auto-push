from collections import deque

n = int(input())
N = deque(list(map(int, input().split())))
cnt = 0
num = 1

while N:
    i = N.popleft()
    if i == num:
        num += 1
    else:
        cnt += 1

print(cnt)