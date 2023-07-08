import math
n, k = map(int, input().split())
m, w = [0]*7, [0]*7
r = 0

for _ in range(n):
    s, y = map(int, input().split())
    if s == 1:
        m[y] += 1
    else :
        w[y] += 1

for i in range(7):
    r += math.ceil(m[i]/k)
    r += math.ceil(w[i]/k)

print(r)