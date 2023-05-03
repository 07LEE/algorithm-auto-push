n = int(input())
cang, sang = 100, 100
for _ in range(n):
    a, b = map(int, input().split())
    if a > b :
        sang -= a
    elif a < b :
        cang -= b
print(cang)
print(sang)