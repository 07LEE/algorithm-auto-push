import sys
input = sys.stdin.readline
n = int(input())
m = sum([int(input())-1 for _ in range(n)]) + 1
print(m)