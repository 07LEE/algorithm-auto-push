x = sorted(list(map(int, input().split())))
if x[0] + x[1] > x[2]:
    print(sum(x))
else :
    print(x[0] + x[1] + x[0] + x[1] - 1)