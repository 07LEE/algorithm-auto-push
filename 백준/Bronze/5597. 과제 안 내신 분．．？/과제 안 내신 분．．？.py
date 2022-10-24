answer = []
data = [input() for _ in range(28)]
for i in range(1,31):
    if str(i) not in data :
        answer.append(i)
for i in answer :
    print(i)