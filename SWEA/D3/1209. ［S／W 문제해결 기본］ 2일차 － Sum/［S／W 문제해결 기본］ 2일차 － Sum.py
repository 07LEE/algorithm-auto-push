T = 10
for t in range(1, T + 1):
    n = int(input())
    answer = []
    arr = [list(map(int, input().split())) for _ in range(100)]
    answer = [sum(i) for i in arr]

    for i in range(100):
        num = 0
        for j in range(100):
            num += arr[j][i]
        answer.append(num)

    for i in range(100):
        num = 0
        num += arr[i][j]
        answer.append(num)

    for i in range(1, 101):
        num = 0
        num += arr[i-1][-i]
        answer.append(num)

    print('#%d %d' %(t, max(answer)))