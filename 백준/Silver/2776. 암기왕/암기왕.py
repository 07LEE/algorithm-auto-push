import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    n = set(map(int, input().split()))
    m = int(input())
    m = list(map(int, input().split()))
    for num in m:
        if num in n:
            print(1)
        else:
            print(0)