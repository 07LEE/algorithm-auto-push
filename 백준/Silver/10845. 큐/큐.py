import sys
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    O = list(input().split())
    if O[0] == 'push' :
        queue.append(O[1])
    if O[0] == 'pop':
        print('-1') if len(queue) == 0 else print(queue.pop(0))
    if O[0] == 'size':
        print(len(queue))
    if O[0] == 'empty':
        print(1) if len(queue) == 0 else print(0)
    if O[0] == 'front':
        print(-1) if len(queue) == 0 else print(queue[0])
    if O[0] == 'back':
        print(-1) if len(queue) == 0 else print(queue[-1])