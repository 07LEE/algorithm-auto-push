n = int(input())
score = [[], [], []]
ans = []
 
for i in range(n):
    a, b, c = map(int, input().split())
    score[0].append(a)
    score[1].append(b)
    score[2].append(c)
    
for i in range(n):
    num = 0
    for j in range(3):
        if score[j].count(score[j][i]) == 1:
            num += score[j][i]
    ans.append(num)

for i in ans:
    print(i)