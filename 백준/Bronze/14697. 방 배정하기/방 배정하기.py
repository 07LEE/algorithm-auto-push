a, b, c, n = map(int, input().split())
count = 0
for i in range(n//a+1):
    for j in range(n//b+1):
        for k in range(n//c+1):
            if a * i + b * j + c * k == n:
                count = 1
print(1) if count == 1 else print(0)
