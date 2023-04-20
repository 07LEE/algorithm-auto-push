from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dq = deque()

for i in range(N):
    command = input().split()
    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)