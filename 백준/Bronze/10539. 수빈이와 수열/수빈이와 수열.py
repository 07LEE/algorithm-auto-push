n = int(input())
a = list(map(int, input().split()))
b = [0]
for i in range(1, n+1):
    b.append(a[i-1] * i - sum(b[:i]))
print(*b[1:])