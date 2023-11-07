N, K = map(int, input().split())
n = [int(str(i*N)[::-1]) for i in range(1, K+1)]
print(max(n))