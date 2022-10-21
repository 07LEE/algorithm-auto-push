c = int(input())
for i in range(c):
    cnt = 0
    data = list(input().split())
    n = int(data[0])
    a = sum(map(int, data[1:]))/n
    for j in map(int, data[1:]):
        if j > a :
           cnt += 1
    print(f'{cnt/n*100:.3f}%')