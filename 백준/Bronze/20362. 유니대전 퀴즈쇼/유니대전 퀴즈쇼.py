n, s = input().split()
w = []
check = True

for _ in range(int(n)):
    a, b = input().split()
    if a == s:
        check = False
        c = b
    else:
        if check is True:
            w.append(b)

print(w.count(c))