P, K = map(int, input().split())
print(P-K+1 if P>K else P+1000-K)