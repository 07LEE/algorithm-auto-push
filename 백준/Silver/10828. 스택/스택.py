import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    O = list(input().split())
    if O[0] == 'push' :
        stack.append(O[1])
    if O[0] == 'pop':
        print('-1') if len(stack) == 0 else print(stack.pop(-1))
    if O[0] == 'size':
        print(len(stack))
    if O[0] == 'empty':
        print(1) if len(stack) == 0 else print(0)
    if O[0] == 'top':
        print('-1') if len(stack) == 0 else print(stack[-1])