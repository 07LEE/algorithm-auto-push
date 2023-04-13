N = int(input())
NS = set(list(map(int, input().split(' '))))
M = int(input())
MS = list(map(int, input().split(' ')))

for i in MS:
    print(1) if i in NS else print(0)