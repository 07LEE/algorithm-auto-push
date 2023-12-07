n = sorted(map(int, input().split()))
a = n[2] - n[1]
b = n[1] - n[0]
if a == b:
    print(n[-1] + a)
else:
    print(n[0] + a)