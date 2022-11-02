T = int(input())
N = []
for _ in range(T) :
    x, y = map(int, input().split())
    N.append([y, x])
N.sort()
[print(i[1], i[0]) for i in N]