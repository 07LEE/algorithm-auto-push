import sys
input = sys.stdin.readline
for _ in range(3):
    N = int(input())
    S = sum([int(input()) for _ in range(N)])
    print(0) if S == 0 else print('+') if S > 0 else print('-')