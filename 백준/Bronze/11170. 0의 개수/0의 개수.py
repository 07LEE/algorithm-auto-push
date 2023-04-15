T = int(input())
for _ in range(T):
    N, M = map(int, input().split(' '))
    answer = 0
    for i in range(N, M+1):
        answer += str(i).count('0')
    print(answer)