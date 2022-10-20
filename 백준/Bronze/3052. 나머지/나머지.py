answer = []
data = [int(input()) for _ in range(10)]
for i in data:
    answer.append(i%42)
print(len(set(answer)))