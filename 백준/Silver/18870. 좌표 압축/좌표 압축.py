N = int(input())
x = list(map(int, input().split()))
ans = []
x_sort = sorted(list(set(x)))
dic = {x_sort[i] : i for i in range(len(x_sort))}
for i in x:
    print(dic[i], end=' ')