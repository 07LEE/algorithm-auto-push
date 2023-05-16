white_paper = [[0] * 100 for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            white_paper[i][j] = 1

black_area = 0
for row in white_paper:
    black_area += sum(row)

print(black_area)