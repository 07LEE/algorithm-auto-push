import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(len(set(a+b))*2 - len(a) - len(b))