M = int(input())
N = [0, 1, 0, 0]
for _ in range(M):
    X, Y = map(int, input().split())
    N[X], N[Y] = N[Y], N[X]
print(N.index(1))