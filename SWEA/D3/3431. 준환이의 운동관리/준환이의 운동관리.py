T = int(input())
for t in range(1, T + 1):
    L, U, X = map(int, input().split())
    ans = -1 if X > U else 0 if L < X< U else L-X
    print('#%d %d'%(t, ans))
