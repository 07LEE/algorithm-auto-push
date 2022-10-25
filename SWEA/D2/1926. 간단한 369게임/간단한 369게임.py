N = int(input())
game = ['3','6','9']
answer = []
for i in range(1, N+1):
    cnt = 0
    for j in game:
        cnt += str(i).count(j)
    answer.append(str(i)) if cnt == 0 else answer.append('-' * cnt)
print(' '.join(answer))