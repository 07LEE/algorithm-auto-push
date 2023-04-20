def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

A, B = map(int, input().split(' '))
print(gcd(A, B))
print(A * B // gcd(A, B))