words = [input() for _ in range(5)]
max_len = max([len(word) for word in words])

for i in range(max_len):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end='')