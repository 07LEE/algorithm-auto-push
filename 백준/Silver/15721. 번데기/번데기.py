A = int(input())
T = int(input())
target = int(input())

a = 0
b = 0
n = 1

check = []

while True:
    for _ in range(2):
        a += 1
        check.append((a, 0))
        b += 1
        check.append((b, 1))
    for _ in range(n + 1):
        a += 1
        check.append((a, 0))
    for _ in range(n + 1):
        b += 1
        check.append((b, 1))

    if a >= T:
        print(check.index((T, target)) % A)
        break

    n += 1