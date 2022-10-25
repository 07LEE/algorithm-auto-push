T = int(input())
for t in range(1, T + 1):
    n = int(input())
    a = sum([i for i in range(1, n+1) if i%2 == 0])
    b = sum([i for i in range(1, n+1) if i%2 != 0])
    print('#%s %s'%(t, b-a))