n, m = map(int, input().split())
X = [list(input()) for _ in range(n)]
x, y = 0, 0

for i in range(n):
    if "X" not in X[i]:
        x += 1

for j in range(m):
    if "X" not in [X[i][j] for i in range(n)]:
        y += 1

print(max(x, y))