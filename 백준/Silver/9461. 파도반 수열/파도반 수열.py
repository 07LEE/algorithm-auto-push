t = int(input())

for _ in range(t):
    n = int(input())
    a = [1] * (n + 1)
    for i in range(3, n+1):
        a[i] = a[i-2] + a[i-3]
    print(a[n-1])