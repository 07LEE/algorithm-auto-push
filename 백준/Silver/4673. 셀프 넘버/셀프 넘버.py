n = list(range(1, 10_001))
remove_n = []

for i in n:
    for j in str(i):
        i += int(j)
    if i <= 10_000:
        remove_n.append(i)

for remove_num in set(remove_n):
    n.remove(remove_num)

for self_num in n:
    print(self_num)
