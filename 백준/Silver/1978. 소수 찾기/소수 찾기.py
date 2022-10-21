n = int(input())
data = list(map(int, input().split()))
cnt = 0
for i in data :
    for j in range(2, i+1):
        if i == j:
            cnt += 1
        if i % j == 0:
            break
print(cnt)