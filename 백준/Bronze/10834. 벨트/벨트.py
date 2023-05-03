n = int(input())
result = 1
t = 0
for _ in range(n):
    a, b ,c = map(int, input().split())
    result = (result//a)*b
    t += c
print(t%2, result)