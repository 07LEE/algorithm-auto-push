import math

n = int(input())
ans = 0

if n == 0 :
    print(0)
elif n == 1:
    print(1)
else:
    print(1 + math.ceil(round(math.log(n, 2), 10)))