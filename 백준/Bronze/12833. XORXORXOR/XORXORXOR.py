a, b, c = map(int, input().split())
for _ in range(c%2):
    a = a ^ b
print(a)