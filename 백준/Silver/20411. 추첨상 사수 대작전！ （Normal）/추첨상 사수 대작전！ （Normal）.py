m, seed, x1, x2 = map(int, input().split())
for a in range(2, m):
    c = (x1 - a * seed) % m
    if (a * x1 + c) % m == x2:
        print(a, c)
        break