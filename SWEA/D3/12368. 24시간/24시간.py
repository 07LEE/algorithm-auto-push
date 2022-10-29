T = int(input())
for t in range(1, T + 1):
    time = sum([i for i in map(int, input().split())])
    print('#%d %d'%(t, time%24))