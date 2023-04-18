L, P = map(int, input().split())
N = list(map(int, input().split()))
[print((i-L*P), end=' ') for i in N]