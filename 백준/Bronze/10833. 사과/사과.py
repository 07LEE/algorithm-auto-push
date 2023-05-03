n = int(input())
resurt = 0
for _ in range(n):
    a, b = map(int, input().split())
    resurt += b%a
print(resurt)