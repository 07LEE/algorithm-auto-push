N = int(input())
K = []
for _ in range(N):
    A, B = map(int, input().split())
    if A <= B :
        K.append(B)
if len(K) != 0:
    print(min(K))
else :
    print('-1')