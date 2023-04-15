T = int(input())
for i in range(T):
    N = list(input().split(' '))
    answer = float(N[0])
    for j in range(1, len(N)):
        if N[j] == '@':
            answer *=3
        elif N[j] == '%':
            answer += 5
        elif N[j] == '#':
            answer -= 7
    print(format(answer, '.2f'))