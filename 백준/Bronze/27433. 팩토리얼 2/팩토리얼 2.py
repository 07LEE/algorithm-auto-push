N = int(input())
if N == 0:
    print(1)
else:
    n = 1
    for i in range(1, N+1):
        n = n * i
    print(n)