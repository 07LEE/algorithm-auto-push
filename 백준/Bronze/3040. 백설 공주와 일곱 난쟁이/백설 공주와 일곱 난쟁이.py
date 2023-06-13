import sys
input = sys.stdin.readline

n = sorted([int(input()) for _ in range(9)])
ans = sum(n) - 100

for i in range(9):
    for j in range(i+1, 9):
        if n[i] + n[j] == ans:
            a, b = i, j
            break

n.remove(n[b])
n.remove(n[a])

[print(i) for i in n]