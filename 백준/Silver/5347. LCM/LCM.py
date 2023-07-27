for _ in range(int(input())):
    a, b = map(int,input().split())
    c = a * b
    while b:
        if a > b:
            a, b = b, a
        b %= a
    print(c // a)