import sys
input = sys.stdin.readline
for i in range(int(input())):
    print(sum(list(map(int, input().split()))))