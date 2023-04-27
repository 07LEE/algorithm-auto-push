a, b = map(int, input().split())
N = []
for i in range(1, b+1):
    for j in range(i):
        N.append(i)
print(sum(N[a-1:b]))