n = list(map(int, input().split()))
m = list(map(int, input().split()))
old = 0

if n[1] < m[1]:
    old = m[0] - n[0]
elif m[1] == n[1]:
    if n[2] <= m[2]:
        old = m[0] - n[0]
    else:
        old = m[0] - n[0] - 1
else:
    old = m[0] - n[0] - 1
print(old)
print(m[0] - n[0] + 1)
print(m[0] - n[0])