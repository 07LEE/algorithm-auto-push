n = int(input())
w = [input() for _ in range(n)]
m = 0

for i in range(n):
    if m != 0:
        break

    word = w[i]
    reversed_word = word[::-1]

    for j in w:
        if reversed_word == j:
            print(len(j), word[len(word)//2])
            m = 1
            break