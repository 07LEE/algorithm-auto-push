t = int(input())
for _ in range(t):
    tmp = []
    n = str(bin(int(input()))[2:])[::-1]
    for i in range(len(n)):
        if n[i] == '1':
            tmp.append(i)
    print(*tmp)