T = int(input())
for _ in range(T):
    word = ''
    W = list(input().split())
    for j in W:
        word += j[::-1]
        word += ' '
    print(word)