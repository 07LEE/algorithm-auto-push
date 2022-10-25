T = int(input())
for t in range(1, T + 1):
    print('#%d %d'%(t, round(sum(list(map(int, input().split())))/10)))