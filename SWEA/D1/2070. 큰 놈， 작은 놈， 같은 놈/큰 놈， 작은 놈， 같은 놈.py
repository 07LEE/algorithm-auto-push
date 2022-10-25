T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    k = '=' if a==b else '>' if a>b else '<'
    print('#%s'%t, k)