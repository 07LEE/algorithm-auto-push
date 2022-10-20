n = int(input())
data = [input().split('X') for _ in range(n)]
for i in range(len(data)):
    answer = 0
    for j in range(len(data[i])):
        for k in range(data[i][j].count('O')+1):
            answer += k
    print(answer)