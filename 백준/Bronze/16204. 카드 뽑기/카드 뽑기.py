N, M, K = map(int, input().split())
O = min([M, K])
X = min([N-M, N-K])
print(O+X)