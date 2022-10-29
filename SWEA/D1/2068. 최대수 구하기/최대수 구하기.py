T = int(input())
for t in range(1, T + 1):
    print('#%d %d'%(t, max([i for i in map(int, input().split())])))