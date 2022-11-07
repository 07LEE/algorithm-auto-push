n = int(input())
m = int(input())
num = []
for i in range(n, m+1):
    for j in range(2, i+1):
        if i == j:
            num.append(i)
        if i % j == 0:
            break
if len(num) != 0:
    print(sum(num))
    print(num[0])
else :
    print(-1)