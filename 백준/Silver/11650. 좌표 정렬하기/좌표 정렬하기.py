T = int(input())
N = sorted([list(map(int, input().split())) for _ in range(T)])
[print(i[0], i[1]) for i in N]