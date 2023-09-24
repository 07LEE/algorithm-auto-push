for _ in range(int(input())):
    g = int(input())
    s = [int(input()) for i in range(g)]
    j = 1
    while True:
        if g == len(set(map(lambda x: x%j, s))):
            print(j)  
            break
        else:
            j += 1