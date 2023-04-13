def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

T = int(input())
for _ in range(T):
    A, B = map(int, input().split(' '))
    print(A * B // gcd(A, B))
