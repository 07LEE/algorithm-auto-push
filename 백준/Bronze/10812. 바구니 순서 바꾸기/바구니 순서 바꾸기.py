n, m = map(int, input().split())
baguni = [i for i in range(1, n+1)]
for _ in range(m):
    i, j, k = map(int, input().split())
    baguni[i-1:j] = baguni[k-1:j] + baguni[i-1:k-1]
print(*baguni)