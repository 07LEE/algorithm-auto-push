n = []
for _ in range(9):
    n.append(int(input()))

num = sum(n) - 100
for i in range(8):
    for j in range(i+1,9):
        if n[i] + n[j] == num:
            one, two = n[i], n[j]
            break


n.remove(one)
n.remove(two)

for i in sorted(n):
    print(i)