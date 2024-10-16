t = int(input())
for _ in range(t):
    n = int(input())
    N = list(map(int, input().split()))
    print(min(N), max(N))