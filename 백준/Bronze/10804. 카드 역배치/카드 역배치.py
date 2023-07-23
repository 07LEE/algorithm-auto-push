n = list(range(21))

for _ in range(10):
    a, b = map(int, input().split())
    for i in range((b-a+1)//2):
        n[a+i], n[b-i] = n[b-i], n[a+i]
print(*n[1:])