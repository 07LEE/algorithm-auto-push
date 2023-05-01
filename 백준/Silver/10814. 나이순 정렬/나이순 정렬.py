N = int(input())
U = []
for _ in range(N):
    U.append(input().split())
U.sort(key=lambda x:int(x[0]))
for i in range(N):
    print(U[i][0], U[i][1])