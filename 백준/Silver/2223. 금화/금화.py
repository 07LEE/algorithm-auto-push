t, x, m = map(int, input().split())
min_x = 1001

for _ in range(m):
    d, s = map(int, input().split())
    if min_x > (d-1)//s:
        min_x = (d-1)//s

if min_x == 0:
    print(0)
elif m == 0:
    print(t * x)
elif t > min_x:
    print((min_x + ((t - min_x)//2)) * x)
else:
    print(t * x)