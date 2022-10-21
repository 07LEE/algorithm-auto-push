import sys
N = int(input())
answer = [int(sys.stdin.readline()) for _ in range(N)]
for i in sorted(answer):
    print(i)