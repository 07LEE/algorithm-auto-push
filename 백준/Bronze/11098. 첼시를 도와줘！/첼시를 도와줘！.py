n = int(input())
for _ in range(n):
    p = int(input())
    max_c = 0
    real_name = ''
    for _ in range(p):
        c, name = input().split()
        if int(c) > max_c:
            max_c = int(c)
            real_name = name
    print(real_name)