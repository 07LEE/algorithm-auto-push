T = int(input())
answer = []
for i in range(T):
    dice = list(map(int, input().split(' ')))
    count = [0] * 7
    for d in dice:
        count[d] += 1
    if max(count) == 3:
        answer.append(10000 + count.index(3) * 1000)
    elif max(count) == 2:
        answer.append(1000 + (count.index(2) * 100))
    else:
        answer.append(max(dice) * 100)
print(max(answer))