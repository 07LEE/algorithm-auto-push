for i in range(10):
    dump = int(input())
    y = sorted(list(map(int, input().split())))
    for _ in range(dump):
        y[0] = y[0] + 1
        y[-1] = y[-1] -1
        y = sorted(y)
    print('#%s %s'%(i+1, (y[-1]-y[0])))