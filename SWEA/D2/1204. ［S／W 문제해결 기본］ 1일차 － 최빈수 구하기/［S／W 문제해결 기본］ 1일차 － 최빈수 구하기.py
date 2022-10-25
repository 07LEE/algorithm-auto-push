T = int(input())
for t in range(1, T + 1):
    N = int(input())
    data = [i for i in map(int, input().split())]
    mode = [data.count(i) for i in set(data)]
    answer = [i for i in set(data) if data.count(i) == max(mode)]
    print('#%d %d'%(t, max(answer)))