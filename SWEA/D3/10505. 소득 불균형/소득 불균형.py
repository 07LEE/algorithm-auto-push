T = int(input())
for t in range(1, T+1):
    N = int(input())
    n = list(map(int, input().split()))
    ans = 0
    for i in n:
        if i <= sum(n)/N :
            ans += 1
    print('#%d %d'%(t, ans))