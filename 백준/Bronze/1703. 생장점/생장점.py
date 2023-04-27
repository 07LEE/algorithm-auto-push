while True:
    a = list(map(int, input().split()))
    leaf = 1
    if a[0] == 0:
        break
    else :
        for i in range(1, len(a), 2):
            leaf =  leaf * a[i] - a[i+1]
        print(leaf)