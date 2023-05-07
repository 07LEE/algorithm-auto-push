winner = 0
score = 0
for i in range(1, 6):
    n = sum(list(map(int, input().split())))
    if n > score:
        winner, score = i, n
print(winner, score)