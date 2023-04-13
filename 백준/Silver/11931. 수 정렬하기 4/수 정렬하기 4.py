import sys
N = int(sys.stdin.readline())
[print(i) for i in sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)]