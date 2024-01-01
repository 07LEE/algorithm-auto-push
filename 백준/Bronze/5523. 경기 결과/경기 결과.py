t = int(input())
A, B = 0, 0
for _ in range(t):
    a, b = map(int, input().split())
    if a > b:
        A += 1
    elif b > a:
        B += 1
    else:
        pass
print(A, B)